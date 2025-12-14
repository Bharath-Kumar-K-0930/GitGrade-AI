def calculate_score(code, commits, repo):
    breakdown = get_score_breakdown(code, commits, repo)
    return min(sum(breakdown.values()), 100)

def get_verdict(score):
    if score >= 85: return "Strong Hire"
    if score >= 70: return "Interview Recommended"
    if score >= 55: return "Maybe / Screen"
    if score >= 40: return "Weak"
    return "Reject"

def get_score_breakdown(code, commits, repo):
    breakdown = {}
    
    # 1. Problem & Product Thinking (15)
    # +15 -> Clear use case (heavier/richer readme keywords)
    # +10 -> Generic
    # +5 -> Toy
    score_prod = 5 # Start at Toy
    readme_content = repo.get("description", "") + " " + code.get("readme_text", "") # Assuming we might have text, or use score
    keywords = ["problem", "solve", "solution", "goal", "purpose", "why", "feature"]
    
    found_keywords = sum(1 for k in keywords if k in readme_content.lower())
    if found_keywords > 3: score_prod = 15
    elif found_keywords > 1 or repo.get("description"): score_prod = 10
    
    # Cap at 15
    breakdown["Problem & Product Thinking"] = score_prod

    # 2. Code Quality & Engineering Maturity (25)
    # Base 25. Deduct for issues.
    score_qual = 25
    
    # Deductions
    # Massive files? (Mock check for 'max_file_lines' or heuristic from complexity)
    if code.get("complexity", 0) > 100: score_qual -= 5 # Heuristic for massive/complex files
    
    # Error handling? (Naive check for try/except in code metrics if available, else assume yes for simplicity or penalty if complexity is weirdly low/high)
    # Let's use complexity as proxy: Very low complexity often means no logic/handling.
    
    # Complexity penalties
    if code.get("complexity", 100) > 50: score_qual -= 5
    
    # "Soft" deduction if file count huge but structured poorly?
    # Ensure min 0
    breakdown["Code Quality & Engineering Maturity"] = max(score_qual, 0)

    # 3. Project Structure & Scalability (15)
    score_struct = 5 # Flat
    if code.get("has_src_folder"): 
        score_struct = 15 # Layered
    elif code.get("file_count", 0) > 5: 
        score_struct = 10 # Logical
    breakdown["Project Structure & Scalability"] = score_struct

    # 4. Git & Collaboration Signals (15)
    score_git = 5 # Inconsistent
    cnt = commits.get("total_commits", 0)
    ratio = commits.get("good_commit_ratio", 0)
    
    if cnt > 15 and ratio > 0.6: score_git = 15 # Atomic + Clean
    elif cnt > 5: score_git = 10 # Decent
    elif cnt <= 1: score_git = 0 # Single commit
    breakdown["Git & Collaboration Signals"] = score_git

    # 5. Testing & Reliability Mindset (10)
    score_test = 0
    if code.get("has_tests"): 
        score_test = 10
        # Check for CI check? If repo has .github/workflows?
        # Assuming fetcher didn't get that specific folder recursively unless deep scan.
        # We'll stick to 'has_tests' flag.
    elif code.get("file_count", 0) > 20: 
        score_test = 3 # Manual likely
    breakdown["Testing & Reliability Mindset"] = score_test

    # 6. Documentation & Communication (10)
    score_doc = 3 # Poor
    rm = code.get("readme_mark", "C")
    if rm == "A": score_doc = 10
    elif rm == "B": score_doc = 6
    else: score_doc = 3
    if not code.get("readme_score"): score_doc = 0
    breakdown["Documentation & Communication"] = score_doc

    # 7. Professionalism Signals (10)
    score_prof = 6 # Mostly clean
    if repo.get("license") and code.get("readme_mark") != "C":
        score_prof = 10
    # Deduct for hardcoded secrets? (If we had a scanner result)
    # We will assume ok for now.
    breakdown["Professionalism Signals"] = score_prof

    return breakdown

def get_level(score):
    return get_verdict(score)
