from radon.complexity import cc_visit
import re

def analyze_code(repo_data: dict):
    files = repo_data["files"]
    
    total_files = len(files)
    has_tests = False
    has_src_folder = False
    
    complexity_score = 0
    
    # Analyze files
    # Note: repo_data["files"] from PyGithub are ContentFile objects
    # We need to act carefully if files is a list of object.
    # The snippet used `f.path` and `f.decoded_content`
    
    for f in files:
        path_lower = f.path.lower()
        if "test" in path_lower or "spec" in path_lower:
            has_tests = True
        if "src" in path_lower or "app" in path_lower:
            has_src_folder = True
            
        # Calculate complexity for Python files
        if f.name.endswith(".py"):
            try:
                content = f.decoded_content.decode('utf-8')
                # cc_visit returns a list of blocks, we sum the complexity
                blocks = cc_visit(content)
                for block in blocks:
                    complexity_score += block.complexity
            except Exception:
                pass
                
    has_readme = repo_data["readme"] is not None
    readme_score = 0
    if has_readme:
        # Simple length heuristic for 0-10 score
        length = len(repo_data["readme"])
        if length > 2000: readme_score = 10
        elif length > 1000: readme_score = 8
        elif length > 500: readme_score = 5
        else: readme_score = 2

    # Average complexity per file (if python exists)
    # This is a bit loose, but follows the requested structure
    
    return {
        "total_files": total_files,
        "has_tests": has_tests,
        "has_readme": has_readme,
        "readme_score": readme_score,
        "has_src_folder": has_src_folder,
        "complexity": complexity_score
    }
