import os
from typing import List

def generate_roadmap(metadata: dict, analysis: dict, score: dict) -> List[str]:
    """
    Generates a personalized improvement roadmap.
    """
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    roadmap = []
    
    # Static logic fallback (always useful even with AI)
    if not analysis.get('has_tests'):
        roadmap.append("Add unit tests to improve code reliability and prevent regressions.")
        
    if score.get('breakdown', {}).get('docs', 0) < 10:
        roadmap.append("Enhance README.md with detailed installation and usage instructions.")
        
    if analysis.get('bad_practices_found') > 0:
        roadmap.append("Refactor code to remove debug prints and handle standard best practices.")
        
    if score.get('breakdown', {}).get('git', 0) < 10:
        roadmap.append("Adopt a clearer commit message convention (e.g., Conventional Commits).")
        
    if not api_key and not roadmap:
         roadmap.append("Review code complexity and modularity.")
         
    # If API key exists, we could enhance this list with LLM suggestions
    
    return roadmap
