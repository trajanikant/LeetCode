import sys
import os
import json
import time
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import pyperclip
import re

# ---------------- CONFIG ----------------
API_URL = "https://leetcode.com/graphql"
PYTHON_DIR = r"F:\Github\LeetCode\Python"
DEFAULT_TOP_N = 5
LOGGING = True  # Set to True to see debug info
# ---------------------------------------

def log(*args):
    if LOGGING:
        print("[LOG]", *args)

def post(query, variables=None):
    data = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = Request(API_URL, data=data, headers={"Content-Type": "application/json","User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as res:
            resp = res.read().decode()
            log("GraphQL response:", resp[:500], "..." if len(resp) > 500 else "")
            return json.loads(resp)
    except HTTPError as e:
        raise Exception(f"HTTP Error {e.code}: {e.reason}")

def resolve_input(arg):
    log("Resolving input:", arg)
    log(f"Input is slug: {arg}")
    return arg

def fetch_problem(slug):
    query = """
    query getQuestion($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        difficulty
        topicTags { name }
        similarQuestions
      }
    }
    """
    log(f"Fetching problem data for slug '{slug}'...")
    resp = post(query, {"titleSlug": slug})
    if "errors" in resp:
        log("GraphQL errors:", resp["errors"])
        raise Exception(f"GraphQL errors: {resp['errors']}")
    question = resp.get("data", {}).get("question")
    if not question:
        raise Exception(f"No data returned for slug '{slug}'")
    log("Problem data fetched successfully")
    return question

def format_similar(similar_json, top_n):
    try:
        data = json.loads(similar_json)
        top = data[:top_n]
        lines = [f'{q["title"]} (https://leetcode.com/problems/{q["titleSlug"]}/)' for q in top]
        return ",\n".join(lines) if lines else "N/A"
    except Exception as e:
        log("Error formatting similar questions:", e)
        return "N/A"

def fetch_problem_live(slug):
    data = fetch_problem(slug)
    # Companies skipped; just N/A
    data["companies"] = {
        "3m": "N/A",
        "6m": "N/A",
        ">6m": "N/A"
    }
    return data

def get_frontend_id(slug):
    # Look in PYTHON_DIR for file matching pattern ****-slug.py
    if not os.path.exists(PYTHON_DIR):
        os.makedirs(PYTHON_DIR)
    pattern = re.compile(r"(\d+)-" + re.escape(slug) + r"\.py$")
    for f in os.listdir(PYTHON_DIR):
        m = pattern.match(f)
        if m:
            return int(m.group(1))
    # If not found, prompt user
    while True:
        try:
            qid = int(input(f"Enter frontend number for slug '{slug}': ").strip())
            # create dummy file to save number
            filename = f"{qid:04d}-{slug}.py"
            filepath = os.path.join(PYTHON_DIR, filename)
            if not os.path.exists(filepath):
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# placeholder for {slug}\n")
            return qid
        except ValueError:
            print("Invalid number. Try again.")

def generate_header(data, top_n=DEFAULT_TOP_N):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    topics = ", ".join(t["name"] for t in data["topicTags"]) or "N/A"
    similar = format_similar(data["similarQuestions"], top_n)
    companies = data.get("companies", {"3m":"N/A","6m":"N/A",">6m":"N/A"})
    qid = get_frontend_id(data["titleSlug"])
    return f'''"""
Problem: {qid:04d}. {data["title"]}
LeetCode Link: https://leetcode.com/problems/{data["titleSlug"]}/description/
Difficulty: {data["difficulty"]}
Topics: {topics}
Companies 3 months: {companies["3m"]}
Companies 6 months: {companies["6m"]}
Companies >6 months: {companies[">6m"]}
Similar Questions (Top {top_n}):
{similar}
Date: {now}
"""'''

def save_to_file(slug, header):
    qid = get_frontend_id(slug)
    filename = f"{qid:04d}-{slug}.py"
    filepath = os.path.join(PYTHON_DIR, filename)
    if os.path.exists(filepath):
        content = open(filepath, "r", encoding="utf-8").read()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(header + "\n\n" + content)
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(header + "\n\n")
    print(f"Saved to {filepath}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python lc.py <problem-slug> [top-N]")
        return
    slug = sys.argv[1].strip()
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_TOP_N
    try:
        slug = resolve_input(slug)
        data = fetch_problem_live(slug)
        header = generate_header(data, top_n)
        print(header)
        pyperclip.copy(header)
        print("\n[Header copied to clipboard!]")
        save_to_file(slug, header)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()