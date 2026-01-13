import os
import sys

# Add the project root to sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime
import time
import argparse
from src.arxiv_client import fetch_latest_papers, filter_papers_by_keywords
from src.llm_client import categorize_and_summarize, generate_daily_highlight, CATEGORIES
from src.content_manager import update_readme, parse_previous_readme

DOMAIN_TAGS = [
    "LLM",
    "Computer Vision",
    "Speech & Audio",
    "Multimodal",
    "Reinforcement Learning",
    "Agents",
    "Robotics",
    "Multi-Agent Systems",
    "Healthcare",
    "Scientific AI",
    "Security",
    "Socio-Economic Systems",
    "Creative AI"
]

def get_tags(text):
    """
    Extracts domain tags from text (title + abstract) using exact string matching.
    """
    text_lower = text.lower()
    found_tags = []
    for tag in DOMAIN_TAGS:
        if tag.lower() in text_lower:
            found_tags.append(tag)
    return found_tags

def main():
    parser = argparse.ArgumentParser(description="AI Safety Paper Curation")
    parser.add_argument('--trial', action='store_true', help="Run in trial mode (output to TRIAL_README.md)")
    parser.add_argument('--date', type=str, help="Specify date in YYYY-MM-DD format", default=None)
    parser.add_argument('--model', type=str, help="Specify LLM model (default: gemini-2.5-flash-lite)", default="gemini-2.5-flash-lite")
    parser.add_argument('--fresh', action='store_true', help="Delete the output file before starting (Fresh start)")
    parser.add_argument('--lag', type=int, help="Number of days to lag behind (target_date = today - lag)", default=4)
    args = parser.parse_args()

    print("Starting AI Safety Paper Curation Process...")
    if args.trial:
        print(" -> MODE: TRIAL")
    if args.date:
        print(f" -> DATE: {args.date}")
    
    target_date = None
    if args.date:
        try:
            target_date = datetime.datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
    elif args.lag > 0:
        # Calculate target date based on lag
        # e.g. lag=4 means target_date is 4 days ago
        target_date = datetime.datetime.now(datetime.timezone.utc).date() - datetime.timedelta(days=args.lag)
        print(f" -> LAG: {args.lag} days (Target Date: {target_date})")

    # 1. Fetch Papers
    print("Fetching papers from arXiv...")
    
    if target_date:
        raw_papers = fetch_latest_papers(target_date=target_date)
    else:
        # Default behavior: last 24h (approx)
        raw_papers = fetch_latest_papers(days_back=1)
        
    print(f"Fetched {len(raw_papers)} papers.")
    
    # 2. Keywise Filter
    potential_papers = filter_papers_by_keywords(raw_papers)
    print(f"Keyword filtering reduced to {len(potential_papers)} papers.")
    
    # Deduplicate by Title (normalized) to match user request explicitly
    # Use title instead of entry_id as user specifically mentioned "same paper (title)"
    seen_titles = set()
    unique_papers = []
    
    for p in potential_papers:
        norm_title = p.title.lower().strip()
        if norm_title not in seen_titles:
            seen_titles.add(norm_title)
            unique_papers.append(p)
            
    potential_papers = unique_papers
    print(f"Deduplication reduced to {len(potential_papers)} papers.")
    
    if not potential_papers:
        print("No matches found.")
        return

    # 3. LLM Processing
    categorized_papers = {cat: [] for cat in CATEGORIES}
    categorized_papers["Other"] = [] # fallback
    
    # Track which categories have updates
    active_categories = set()
    
    print("Processing papers with LLM...")
    llm_call_count = 0
    for paper in potential_papers:
        if llm_call_count > 0 and llm_call_count % 5 == 0:
            print("Rate limit pause: Sleeping for 60 seconds...")
            time.sleep(60)
            
        print(f"Analyzing: {paper.title}...")
        
        # Prepare data for LLM
        analysis = categorize_and_summarize(paper.title, paper.summary, model_name=args.model)
        llm_call_count += 1
        
        if analysis.get("relevant"):
            cat = analysis.get("category")
            # Normalize category if LLM hallucinates slightly or if it's new
            # For now we trust the list or use Other
            if cat not in CATEGORIES:
                cat = "Other"
            
            # Determine tags locally
            full_text = f"{paper.title} {paper.summary}"
            tags = get_tags(full_text)
            
            paper_data = {
                "title": paper.title,
                "summary": analysis.get("summary", ""),
                "tags": tags,
                "link": paper.entry_id,
                "published": paper.published
            }
            
            categorized_papers[cat].append(paper_data)
            active_categories.add(cat)
            print(f" -> Added to {cat}")
        else:
            print(" -> Not relevant.")
            
    # 4. Generate Category Highlights
    daily_highlights_map = {}
    print("Generating category highlights...")
    for cat in active_categories:
        papers_in_cat = categorized_papers[cat]
        if papers_in_cat:
            highlight = generate_daily_highlight(cat, papers_in_cat, model_name=args.model)
            daily_highlights_map[cat] = highlight
            
    # 5. Update Content
    # If explicit date is set, use that. Else use today.
    if target_date:
        date_str = target_date.strftime("%Y-%m-%d")
    else:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        
    output_file = "TRIAL_README.md" if args.trial else "README.md"
    
    existing_papers = {}
    existing_highlights_map = {}
    existing_overall_highlight = ""

    if args.fresh:
        if os.path.exists(output_file):
            print(f"Fresh start: Deleting {output_file}...")
            os.remove(output_file)
    else:
        print(f"Loading existing content from {output_file}...")
        existing_papers, existing_overall_highlight, existing_highlights_map = parse_previous_readme(output_file)
        
        # Deduplicate existing vs new:
        # We will check if the new papers are already in existing_papers to avoid duplicates
        # The 'seen_titles' set earlier only deduped the *fetched* batch against itself.
        # We need to expand seen_titles or check before adding.
        
        # Actually simpler: We already have 'potential_papers' which are the filtered, deduplicated *new* batch.
        # We should proceed to process them, then merge.

    # Merge new papers into existing papers (Prepend new ones)
    final_categorized_papers = existing_papers.copy()
    
    # Initialize tags for categories not in existing
    for cat in CATEGORIES + ["Other"]:
        if cat not in final_categorized_papers:
            final_categorized_papers[cat] = []
            
    # Add new papers to the front
    for cat, new_list in categorized_papers.items():
        if not new_list: continue
        
        # Filter duplicates
        # Get set of existing titles for this category
        existing_titles = {p['title'].lower().strip() for p in final_categorized_papers[cat]}
        
        unique_new = []
        for p in new_list:
             if p['title'].lower().strip() not in existing_titles:
                 unique_new.append(p)
                 
        if unique_new:
             final_categorized_papers[cat] = unique_new + final_categorized_papers[cat]

    # 4. Generate Highlights (Weekly on Sunday)
    # Check if target_date (or today) is Sunday. Sunday is weekday() 6.
    current_date = target_date if target_date else datetime.datetime.now().date()
    is_sunday = (current_date.weekday() == 6)
    
    daily_highlights_map = existing_highlights_map.copy()
    
    if is_sunday:
        print("It is Sunday! Generating Weekly Summaries...")
        cutoff_date = current_date - datetime.timedelta(days=7)
        
        # Re-scan active categories based on merged list
        for cat, papers in final_categorized_papers.items():
            recent_papers = []
            for p in papers:
                p_date = p.get('published')
                # Parse if it's a string (from parser) or date/datetime
                if isinstance(p_date, str):
                    try:
                        p_date = datetime.datetime.strptime(p_date, "%Y-%m-%d").date()
                    except:
                        continue
                elif isinstance(p_date, datetime.datetime):
                    p_date = p_date.date()
                
                if p_date and p_date >= cutoff_date and p_date <= current_date:
                    recent_papers.append(p)
            
            if recent_papers:
                print(f"Summarizing {cat} ({len(recent_papers)} papers from last week)...")
                highlight = generate_daily_highlight(cat, recent_papers, model_name=args.model)
                daily_highlights_map[cat] = highlight
                
    else:
        print("Not Sunday. Keeping existing summaries.")
        # If we have new papers but no existing highlight, maybe generate one?
        # User requested "only a run on Sunday will update the summary".
        # So we strictly respect existing unless Sunday.
        # But if it's a fresh start on a Monday? existing is empty.
        # In that case, we should probably generate an initial summary.
        # Let's add a check: if highlight missing and we have papers, generate it.
        for cat in active_categories:
            if cat not in daily_highlights_map or not daily_highlights_map[cat]:
                 papers_in_cat = categorized_papers[cat]
                 if papers_in_cat:
                     daily_highlights_map[cat] = generate_daily_highlight(cat, papers_in_cat, model_name=args.model)

    # 5. Update Content
    date_str = current_date.strftime("%Y-%m-%d")

    print(f"Updating {output_file}...")
    update_readme(date_str, final_categorized_papers, daily_highlights_map, file_path=output_file)
    print("Done!")


if __name__ == "__main__":
    main()
