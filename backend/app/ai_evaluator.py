import os
# from openai import OpenAI # specific import if using openai library

def generate_summary(metadata: dict, analysis: dict, score: dict) -> str:
    """
    Generates a concise evaluation summary using an LLM.
    """
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    # Construct the prompt context
    context = f"""
    Repository Metrics:
    - Language: {metadata.get('language')}
    - Files: {analysis.get('total_files')}
    - Tests: {'Yes' if analysis.get('has_tests') else 'No'}
    - Score: {score.get('total_score')}/100
    - Bad Practices Found: {analysis.get('bad_practices_found')}
    """
    
    if not api_key:
        # Fallback if no API key
        return f"The repository demonstrates basic functionality with a score of {score.get('total_score')}/100. It is written in {metadata.get('language')}. (AI Summary requires API Key)"

    # Mock implementation of LLM call
    # In a real scenario, you would call client.chat.completions.create(...)
    
    return f"The repository is a {metadata.get('language')} project with {analysis.get('total_files')} files. It scores {score.get('total_score')}/100. Improvements are needed in documentation and testing to ensure reliability."
