from github import Github
import os

def get_github_client():
    token = os.getenv("GITHUB_TOKEN")
    if not token or token.strip() == "":
        token = None
    return Github(token)

def fetch_repo_data(repo_url: str):
    """
    Fetches comprehensive repository data using PyGithub.
    """
    g = get_github_client()
    
    import re
    try:
        # Regex to match owner/repo from various formats:
        # https://github.com/owner/repo
        # github.com/owner/repo
        # owner/repo
        
        # Strip trailing .git
        clean_url = repo_url.strip().rstrip(".git")
        
        match = re.search(r'github\.com[:/]([^/]+)/([^/]+)', clean_url)
        if match:
            owner, repo_name = match.groups()
        else:
            # Try splitting by slash if it looks like owner/repo
            parts = clean_url.split('/')
            if len(parts) >= 2:
                owner, repo_name = parts[-2], parts[-1]
            else:
                 raise ValueError("Invalid GitHub URL format")
        
        print(f"Parsed Owner: {owner}, Repo: {repo_name}")
        
        # Attempt to get repo
        repository = g.get_repo(f"{owner}/{repo_name}")
        print(f"Successfully fetched repo object: {repository.name}")
        
        # Get language breakdown
        languages = repository.get_languages()
        
        # Get readme
        try:
            readme = repository.get_readme().decoded_content.decode()
        except:
            readme = None
            
        # Get top-level files (simplification for "files")
        # For deep analysis we might need recursive, but "get_contents('')" is per spec
        files = repository.get_contents("")
        
        return {
            "name": repository.name,
            "stars": repository.stargazers_count,
            "forks": repository.forks_count,
            "languages": languages,
            "files": files, # List of ContentFile objects
            "readme": readme,
            "default_branch": repository.default_branch,
            "has_api": True # Mock or check strictly
        }
    except Exception as e:
        return {"error": str(e)}
