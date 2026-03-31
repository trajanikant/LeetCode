import sys
import os
import json
import re
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import pyperclip

# ---------------- CONFIG ----------------
API_URL = "https://leetcode.com/graphql"
PYTHON_DIR = r"F:\Github\LeetCode\Python"
DEFAULT_TOP_N = 5
LOGGING = True
# ---------------------------------------

def log(*args):
    if LOGGING:
        print("[LOG]", *args)

# ---------- NETWORK / API ----------
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
        raise Exception(f"GraphQL errors: {resp['errors']}")
    question = resp.get("data", {}).get("question")
    if not question:
        raise Exception(f"No data returned for slug '{slug}'")
    log("Problem data fetched successfully")
    return question

# ---------- COMPANY BLOCK FORMATTING ----------
def format_companies_block(raw_lines: list) -> dict:
    """Convert multi-line company block into structured inline dictionary safely."""
    result = {"3m": "", "6m": "", ">6m": ""}
    current_key = None
    temp_list = []
    mapping = {"3 months": "3m", "6 months": "6m", ">6 months": ">6m"}

    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        if any(line.startswith(k) for k in mapping):
            if current_key and temp_list:
                if len(temp_list) % 2 != 0:
                    temp_list.append("N/A")
                result[current_key] = ", ".join(
                    f"{temp_list[i]} - {temp_list[i+1]}" for i in range(0, len(temp_list), 2)
                )
            for k, v in mapping.items():
                if line.startswith(k):
                    current_key = v
                    break
            temp_list = []
        else:
            temp_list.append(line)
    # final block
    if current_key and temp_list:
        if len(temp_list) % 2 != 0:
            temp_list.append("N/A")
        result[current_key] = ", ".join(
            f"{temp_list[i]} - {temp_list[i+1]}" for i in range(0, len(temp_list), 2)
        )
    return result

def update_companies_in_file(filepath):
    """Detect and reformat the company block in an existing file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    header_match = re.search(r'3 months\s*:(.*?)>6 months\s*:.*?(?=Similar Qs)', content, re.S)
    if not header_match:
        return

    raw_block = header_match.group(0)
    raw_lines = [line.strip() for line in raw_block.splitlines() if line.strip()]
    formatted_companies = format_companies_block(raw_lines)

    new_block = (
        f"3 months    : {formatted_companies.get('3m', 'N/A')}\n"
        f"6 months    : {formatted_companies.get('6m', 'N/A')}\n"
        f">6 months   : {formatted_companies.get('>6m', 'N/A')}\n\n"
    )

    new_content = content.replace(raw_block, new_block)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated companies in {os.path.basename(filepath)}")

def update_all_other_files(current_file):
    """Update company blocks for all files except the current file."""
    for filename in os.listdir(PYTHON_DIR):
        # if filename.endswith(".py") and filename != current_file:
        if filename.endswith(".py"):
            update_companies_in_file(os.path.join(PYTHON_DIR, filename))

# ---------- HEADER GENERATION ----------
def get_frontend_id(slug):
    if not os.path.exists(PYTHON_DIR):
        os.makedirs(PYTHON_DIR)
    pattern = re.compile(r"(\d+)-" + re.escape(slug) + r"\.py$")
    for f in os.listdir(PYTHON_DIR):
        m = pattern.match(f)
        if m:
            return int(m.group(1))
    while True:
        try:
            qid = int(input(f"Enter frontend number for slug '{slug}': ").strip())
            filename = f"{qid:04d}-{slug}.py"
            filepath = os.path.join(PYTHON_DIR, filename)
            if not os.path.exists(filepath):
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# placeholder for {slug}\n")
            return qid
        except ValueError:
            print("Invalid number. Try again.")

def generate_header(data, time_taken="N/A", revision="N", top_n=DEFAULT_TOP_N):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    topics = ", ".join(t["name"] for t in data.get("topicTags", [])) or "N/A"

    try:
        similar_json = data.get("similarQuestions", "[]")
        similar_list = json.loads(similar_json)
        similar_top = similar_list[:top_n]
        similar_str = ",\n".join(
            f'{q["title"]} (https://leetcode.com/problems/{q["titleSlug"]}/)'
            for q in similar_top
        ) if similar_top else "N/A"
    except Exception:
        similar_str = "N/A"

    companies = {"3m": "N/A", "6m": "N/A", ">6m": "N/A"}
    qid = get_frontend_id(data["titleSlug"])

    header = f'''"""
Problem     : {qid:04d}. {data["title"]}
Link        : https://leetcode.com/problems/{data["titleSlug"]}/description/
Difficulty  : {data.get("difficulty", "N/A")}
Topics      : {topics}

3 months    : {companies.get("3m")}
6 months    : {companies.get("6m")}
>6 months   : {companies.get(">6m")}

Similar Qs  :
{similar_str}

Time Taken  : {time_taken}
Date        : {now}
Revision    : {revision}
"""
'''
    return header

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
    return filename  # return current file for skipping

# ---------- MAIN ----------
def main():
    if len(sys.argv) < 2:
        print("Usage: python lc.py <problem-slug> [top-N] [time-taken] [revision]")
        return

    slug = sys.argv[1].strip()
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_TOP_N
    time_taken = sys.argv[3] if len(sys.argv) > 3 else "N/A"
    revision = sys.argv[4] if len(sys.argv) > 4 else "N"

    try:
        slug = resolve_input(slug)
        data = fetch_problem(slug)
        header = generate_header(data, time_taken=time_taken, revision=revision, top_n=top_n)
        print(header)
        pyperclip.copy(header)
        print("\n[Header copied to clipboard!]")
        current_file = save_to_file(slug, header)
        # Reformat all other files' company blocks
        update_all_other_files(current_file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()