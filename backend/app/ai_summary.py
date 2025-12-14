from openai import OpenAI
import os
from app.feedback_engine import derive_facts

def generate_summary(repo: dict, code: dict, commits: dict) -> str:
    """
    Generates a recruiter-style summary by asking AI to explain the derived facts.
    Facts -> Narrative.
    """
    facts = derive_facts(code, commits, repo)
    strengths = facts["strengths"]
    weaknesses = facts["weaknesses"]
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Construction of the prompt context
    strength_text = "\n".join([f"- {s}" for s in strengths]) if strengths else "- None identified"
    weakness_text = "\n".join([f"- {w}" for w in weaknesses]) if weaknesses else "- None identified"

    if not api_key:
        # Deterministic Mirror (Fallback)
        # We manually construct sentences from the first few facts
        summary = "Analysis Results: "
        if strengths:
            summary += f"The repository demonstrates {strengths[0].lower()} and {strengths[1].lower() if len(strengths)>1 else 'good fundamentals'}. "
        
        if weaknesses:
            summary += f"However, {weaknesses[0].lower()} and {weaknesses[1].lower() if len(weaknesses)>1 else 'improvements are needed'}. "
        elif strengths:
            summary += "It shows strong engineering maturity overall."
            
        return summary.strip()

    client = OpenAI(api_key=api_key)
    
    prompt = f"""
    You are a generic Repository Mirror. 
    Review these FACTS about a GitHub repository and write a 2-sentence professional recruiter evaluation.
    
    STRENGTHS:
    {strength_text}
    
    WEAKNESSES:
    {weakness_text}
    
    TASK:
    Convert these bullet points into a cohesive, professional narrative. 
    Do NOT invent new attributes. Reflect ONLY these facts.
    Balance the tone: verify quality but be honest about gaps.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"The project shows {len(strengths)} strengths (e.g., {strengths[0] if strengths else 'N/A'}) but has {len(weaknesses)} areas for improvement ({weaknesses[0] if weaknesses else 'N/A'})."
