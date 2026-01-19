import arxiv
from datetime import datetime, timedelta, timezone

# Keywords to initially filter papers.
# We cast a wide net here; the LLM will do the precision filtering.
SAFETY_KEYWORDS = [
    "AI safety",
    "AI wellbeing",
    "value alignment",
    "outer alignment",
    "inner alignment",
    "alignment failure",
    "misaligned objectives",
    "specification failure",
    "reward hacking",
    "reward misspecification",
    "specification gaming",
    "objective misspecification",
    "jailbreak",
    "prompt injection",
    "prompt hacking",
    "constitutional AI",
    "superalignment",
    "scalable alignment",
    "scalable oversight",
    "AI control problem",
    "red teaming",
    "alignment evaluation",
    "alignment benchmarks",
    "corrigibility",
    "shutdownability",
    "human oversight",
    "deceptive alignment",
    "deceptive behavior",
    "deception",
    "goal misgeneralization",
    "mesa-optimization",
    "mesa-optimizers",
    "instrumental convergence",
    "instrumental goals",
    "power-seeking behavior",
    "power-seeking",
    "emergent misalignment",
    "alignment failure modes",
]

def fetch_latest_papers(days_back=1, target_date=None):
    """
    Fetches CS papers from arXiv.
    If target_date is provided (datetime.date), fetches for that specific day (UTC).
    Otherwise, fetches from the last `days_back` days.
    """
    client = arxiv.Client()
    
    # Query specifically for AI and Machine Learning categories
    # OR logic allowed in arXiv API: cat:cs.AI OR cat:cs.LG
    search_query = '(cat:cs.AI OR cat:cs.LG)'
    
    if target_date:
        date_str = target_date.strftime("%Y%m%d")
        # Overwrite search query for specific date to ensure we get them
        search_query += f' AND submittedDate:[{date_str}0000 TO {date_str}2359]'
        
    search = arxiv.Search(
        query=search_query,
        max_results=500, # Increase fetch size to ensure coverage when filtering by date
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    
    results = []

    if target_date:
        # The query prevents fetching outside the date range, but we iterate to collect them
        for result in client.results(search):
            results.append(result)
    else:
        # Default behavior: last N days
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
        
        for result in client.results(search):
            # The published date is a datetime object with timezone info
            if result.published < cutoff_date:
                break
                
            results.append(result)
        
    return results

def filter_papers_by_keywords(papers):
    """
    Filters papers that look relevant based on keywords in title or abstract.
    """
    filtered = []
    for paper in papers:
        text_to_check = (paper.title + " " + paper.summary).lower()
        if any(keyword in text_to_check for keyword in SAFETY_KEYWORDS):
            filtered.append(paper)
    return filtered

if __name__ == "__main__":
    # Smoke test
    print("Fetching papers...")
    papers = fetch_latest_papers(days_back=1)
    print(f"Fetched {len(papers)} papers.")
    filtered = filter_papers_by_keywords(papers)
    print(f"Filtered down to {len(filtered)} potential safety papers.")
    for p in filtered:
        print(f"- {p.title}")
