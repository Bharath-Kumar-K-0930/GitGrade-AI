from app.feedback_engine import derive_facts, generate_rule_roadmap

def generate_roadmap(score: int, code: dict, commits: dict) -> list:
    """
    Generates a personalized improvement roadmap based on strict rules.
    condition -> action
    """
    # Derive facts (Weaknesses)
    # We pass empty repo dict as it's not crucial for these specific rules yet, or pass minimal
    facts = derive_facts(code, commits, {})
    
    # Generate Roadmap from Weaknesses
    return generate_rule_roadmap(facts["weaknesses"])
