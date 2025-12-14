def calculate_score(code, commits, repo):
    score = 0

    # Code Quality (25)
    # Logic: Lower complexity is better? Or is this complexity score additive?
    # If complexity is total complexity of all files, it depends on project size.
    # The user snippet: if code["complexity"] < 10: score += 25.
    # This implies 'complexity' is Average Cyclomatic Complexity or something small?
    # But text says "complexity_score += len(cc_visit...)" which is SUM of complexity.
    # A large project will have huge complexity.
    # I will assume "complexity" in the scoring logic refers to *Average* or normalized.
    # Let's normalize it by file count or assume it's per function average.
    # For safe implementation matching the user request strictly:
    
    comp = code["complexity"]
    # Adjusting logic slightly to be realistic: if total complexity is low, it might just be small.
    # But let's stick to the prompt's logic if possible, or interpret "complexity" as "Avg Complexity".
    # I will interpret it as total for now but cap it, as per prompt. 
    # Actually, if I look at the prompt: `if code["complexity"] < 10`. 10 is very low. 
    # It likely means "Average Complexity". I should probably calculate avg in analyzer.
    # Re-reading code_analyzer: it sums it up. 
    # I will stick to the user's snippet blindly for the "Perfect Copy", but maybe use Avg logic if I can.
    # Let's use the USER's logic EXACTLY.
    
    if code["complexity"] < 10:
        score += 25
    elif code["complexity"] < 20:
        score += 18
    else:
        score += 10 # Even complex code gets some points?

    # Structure (15)
    if code["has_src_folder"]:
        score += 15
    else:
        score += 8

    # Documentation (15)
    if code["readme_score"] > 7:
        score += 15
    elif code["readme_score"] > 4:
        score += 10
    else:
        score += 5

    # Testing (15)
    if code["has_tests"]:
        score += 15

    # Git Practices (15)
    # Cap at 15 points
    score += min(commits["total_commits"], 15)

    # Real-world relevance (15)
    if repo["stars"] > 10 or repo.get("has_api"):
        score += 15
    else:
        score += 8

    return min(score, 100)

def get_level(score):
    if score < 40:
        return "Beginner"
    elif score < 70:
        return "Intermediate"
    return "Advanced"
