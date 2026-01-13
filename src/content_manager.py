import os
from datetime import datetime

README_PATH = "README.md"
ARCHIVE_DIR = "archives"

# Template for the README
README_HEADER = """# arXiv curation - AI Safety

Curation of arXiv papers related to AI Safety, categorized and summarized by LLM.

## Overview ({date})
{daily_highlights}

## Latest Papers ({date})
"""

CATEGORY_TABLE_HEADER = """
### {category}
{highlight}

| Date | Title | Tags | Summary |
|---|---|---|---|
"""

def update_readme(date_str, categorized_papers, daily_highlights_map, file_path=README_PATH):
    """
    Regenerates the README with the latest content.
    categorized_papers: dict {category_name: [list of paper dicts]}
    daily_highlights_map: dict {category_name: highlight_text}
    file_path: Output file path (default: README.md)
    """
    
    # Construct the Highlights section
    overall_highlights = ""
    for cat, highlight in daily_highlights_map.items():
        if highlight:
            overall_highlights += f"- **{cat}**: {highlight}\n"
            
    if not overall_highlights:
        overall_highlights = "No significant updates today."

    content = README_HEADER.format(date=date_str, daily_highlights=overall_highlights)
    
    # Construct the tables
    # Sort categories to ensure fixed order if desired, or use the order from keys
    for category in sorted(categorized_papers.keys()):
        papers = categorized_papers[category]
        if not papers:
            continue
            
        highlight = daily_highlights_map.get(category, "")
        if highlight:
            formatted_highlight = f"_{highlight}_\n"
        else:
            formatted_highlight = ""
            
        content += CATEGORY_TABLE_HEADER.format(category=category, highlight=formatted_highlight)
        
        for paper in papers:
            # Escape pipes in title/summary to avoid breaking table
            title = paper['title'].replace("|", "\|")
            summary = paper['summary'].replace("|", "\|")
            link = paper.get('link', '#')
            
            # Format date (YYYY-MM-DD)
            pub_date = paper.get('published').strftime("%Y-%m-%d") if paper.get('published') else ""
            
            # Format tags
            tags_list = paper.get('tags', [])
            tags_str = ", ".join(tags_list) if tags_list else ""
            
            content += f"| {pub_date} | [{title}]({link}) | {tags_str} | {summary} |\n"
    
    with open(file_path, "w") as f:
        f.write(content)
        
import re

def parse_previous_readme(file_path):
    """
    Parses the existing README to extract:
    1. Overall Highlights (Most Notable Developments)
    2. Category Highlights
    3. Existing Papers (per category)
    
    Returns:
        tuple: (existing_papers_dict, existing_overall_highlights, existing_category_highlights_map)
    """
    if not os.path.exists(file_path):
        return {}, "", {}
        
    with open(file_path, "r") as f:
        content = f.read()
        
    # 1. Extract Overall Highlights
    # Look for content between "## Overview..." and "## Latest Papers..."
    overall_highlights = ""
    overall_match = re.search(r"## Overview.*?\n(.*?)\n## Latest Papers", content, re.DOTALL)
    if overall_match:
        overall_highlights = overall_match.group(1).strip()
        
    # 2. Extract Categories Sections
    # Split by "### " headers
    category_parts = re.split(r"\n### ", content)
    # Skip the first part (header stuff)
    
    existing_papers = {}
    existing_cat_highlights = {}
    
    # We need to skip the preamble. The first split might contain the headers.
    # A safer way might be to iterate through known categories or regex scan.
    # Let's try regex for blocks: "### {Category}\n{Highlight}\n\n| Table..."
    
    # The categories are dynamic, so let's iterate over what we find.
    # Regex to capture: Category Name, Optional Highlight, Table Body
    # Table body starts with | Date |
    
    # Strategy: Find all sections strictly.
    # Pattern: ### (Category Name)\n(Optional Italic Highlight\n)?\n| Date...
    
    # Simpler: Split by "### "
    # First chunk is README header + Overall.
    # Subsequent chunks are "Category \n ... table"
    
    for chunk in category_parts[1:]:
        lines = chunk.strip().split('\n')
        if not lines:
            continue
            
        category_name = lines[0].strip()
        
        # Check for highlight (starts with _)
        highlight = ""
        table_start_idx = -1
        
        for i, line in enumerate(lines[1:], 1):
            if line.strip().startswith('_') and line.strip().endswith('_'):
                highlight = line.strip().strip('_')
            if line.strip().startswith('| Date |'):
                table_start_idx = i
                break
        
        if highlight:
            existing_cat_highlights[category_name] = highlight
            
        papers_list = []
        if table_start_idx != -1:
            # Parse table rows
            # Skip header and separator
            for line in lines[table_start_idx+2:]:
                if not line.strip().startswith('|'): 
                    continue
                
                # Expected format: | Date | [Title](Link) | Tags | Summary |
                cols = [c.strip() for c in line.split('|')[1:-1]]
                if len(cols) >= 4:
                    date_str = cols[0]
                    title_link = cols[1]
                    tags_str = cols[2]
                    summary = cols[3]
                    
                    # Extract title and link
                    link_match = re.match(r"\[(.*?)\]\((.*?)\)", title_link)
                    if link_match:
                        title = link_match.group(1).replace("\|", "|")
                        link = link_match.group(2)
                    else:
                        title = title_link
                        link = "#"
                        
                    tags = [t.strip() for t in tags_str.split(',')] if tags_str else []
                    
                    try:
                        pub_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    except:
                        pub_date = None
                        
                    papers_list.append({
                        "title": title,
                        "summary": summary.replace("\|", "|"),
                        "tags": tags,
                        "link": link,
                        "published": pub_date,
                        "date_str": date_str # Keep original string for creating datetime object
                    })
        
        existing_papers[category_name] = papers_list
        
    return existing_papers, overall_highlights, existing_cat_highlights

def archive_daily_content(date_str, content):
    """
    Saves the daily content to an archive file. 
    (Future implementation: append to a monthly archive or create daily files)
    """
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
        
    filepath = os.path.join(ARCHIVE_DIR, f"{date_str}.md")
    with open(filepath, "w") as f:
        f.write(content)
