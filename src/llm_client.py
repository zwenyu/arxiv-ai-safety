
import os
from google import genai
from google.genai import types
import json
import logging

CATEGORIES = [
    "Alignment",
    "Robustness & Generalization",
    "Interpretability",
    "Control & Corrigibility",
    "Agentic & Long-Horizon Risks",
    "Evaluation & Benchmarking",
    "Multi-Agent & Societal Dynamics",
    "Misuse & Security",
    "Governance & Policy",
    "Ethics & Human Values",
    "Scalable Alignment & Existential Risk"
]

CATEGORY_STRING = "\n".join([f"- {c}" for c in CATEGORIES])

def get_client():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        logging.warning("GOOGLE_API_KEY not found in environment variables.")
        return None
    return genai.Client(api_key=api_key)

DEFAULT_MODEL = "gemini-2.5-flash-lite"

def categorize_and_summarize(paper_title, paper_abstract, model_name=DEFAULT_MODEL):
    """
    Uses Gemini Flash to analyze a paper.
    Returns a dict with:
      - relevant (bool): Is it related to AI Safety?
      - category (str): One of the defined categories or "Other"
      - summary (str): One sentence summary
      - explanation (str): Why it fits the category (optional, for debugging)
    """
    client = get_client()
    if not client:
        return {"relevant": False, "category": "Error", "summary": "Missing API Key", "explanation": "Missing API Key"}

    prompt = f"""
    You are an expert AI Safety researcher curating papers for a daily report.
    Analyze the following paper to see if it is highly relevant to AI Safety / AIS (Artificial Intelligence Safety).
    
    Paper Title: {paper_title}
    Abstract: {paper_abstract}
    
    List of AI Safety Categories:
    {CATEGORY_STRING}
    
    Task:
    1. Determine if this paper is relevant to AI Safety. If it is just general ML performance without a safety angle, mark it as not relevant.
    2. Assign it to ONE of the categories above. If it is relevant but fits none, choose the closest one or "Other".
    3. Based on the abstract, write a ONE SENTENCE concise summary of the main novelty/insight of the paper.
    
    Output JSON format:
    {{
      "relevant": true/false,
      "category": "Category Name",
      "summary": "One sentence summary...",
      "explanation": "Reasoning..."
    }}
    """
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error processing {paper_title}: {e}")
        return {"relevant": False, "category": "Error", "summary": "", "explanation": str(e)}

def generate_daily_highlight(category, papers, model_name=DEFAULT_MODEL):
    """
    Generates a snippet describing the trends/notable papers for a category.
    """
    if not papers:
        return ""
    
    client = get_client()
    if not client:
        return f"Updated with {len(papers)} new papers."

    paper_list = "\n".join([f"- {p['title']}: {p['summary']}" for p in papers])
    
    prompt = f"""
    Here are the recent AI Safety papers for the category '{category}' (from the past week):
    {paper_list}
    
    Write a short paragraph (2-3 sentences) summarizing specific key developments in this area. Focus on the actual content of the papers. Start the summary with "This week's papers...".
    """
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Updated with {len(papers)} new papers."
