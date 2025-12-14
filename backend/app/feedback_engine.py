def derive_facts(code, commits, repo):
    """
    Analyzes metrics and returns a dictionary of factual Strengths and Weaknesses.
    Rules decide facts.
    """
    strengths = []
    weaknesses = []
    
    # 1. Structure
    if code.get("has_src_folder"):
        strengths.append("Standard 'src' folder structure detected")
    elif code.get("file_count", 0) > 5 and not code.get("has_src_folder"):
        weaknesses.append("Flat file structure (missing 'src' folder)")
        
    # 2. Documentation
    if code.get("readme_score", 0) > 8:
        strengths.append("Comprehensive README with setup and usage details")
    elif code.get("readme_score", 0) > 4:
         weaknesses.append("Basic README found (could be more detailed)")
    else:
        weaknesses.append("Missing or empty README")
        
    # 3. Testing
    if code.get("has_tests"):
        strengths.append("Automated tests detected")
    else:
        weaknesses.append("No automated tests found")
        
    # 4. Git Hygiene
    if commits.get("good_commit_ratio", 0) > 0.7:
        strengths.append("Clean and meaningful commit history")
    elif commits.get("good_commit_ratio", 0) < 0.4:
        weaknesses.append("Inconsistent commit messages")
        
    # 5. Quality
    if code.get("complexity", 100) < 15:
        strengths.append("Code functions are concise and readable")
    elif code.get("complexity", 100) > 50:
        weaknesses.append("High code complexity detected (large functions)")
        
    return {"strengths": strengths, "weaknesses": weaknesses}

def generate_rule_roadmap(weaknesses):
    """
    Generates a personalized roadmap based PURELY on identified weaknesses.
    Condition -> Action.
    """
    roadmap = []
    
    for w in weaknesses:
        if "structure" in w:
            roadmap.append("Refactor project: Move source code into a 'src/' directory")
        if "README" in w:
            roadmap.append("Improve README: Add 'Installation', 'Usage', and 'Tech Stack' sections")
        if "tests" in w:
            roadmap.append("Add unit tests: Create a 'tests/' folder and add basic assertions")
        if "commit" in w:
            roadmap.append("Adopt conventional commits: Use prefixes like 'feat:', 'fix:', 'docs:'")
        if "complexity" in w:
            roadmap.append("Refactor code: Break down large functions into smaller, reusable components")
            
    # Default if empty
    if not roadmap:
        roadmap.append("Review project architecture for scalability")
        roadmap.append("Set up comprehensive CI/CD pipeline")
        
    return roadmap
