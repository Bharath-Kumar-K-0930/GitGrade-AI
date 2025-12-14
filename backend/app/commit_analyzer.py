from github import Github
import os

def get_github_client():
    token = os.getenv("GITHUB_TOKEN")
    return Github(token)

def analyze_commits(repo_url: str):
    g = get_github_client()
    try:
        owner, repo = repo_url.replace("https://github.com/", "").split("/")
        repository = g.get_repo(f"{owner}/{repo}")

        # Get last 20 commits
        commits = repository.get_commits()
        total_commits = commits.totalCount # This might be slow for large repos, but per spec
        
        # Taking slicing on PaginatedList fetches those items
        recent_commits = commits[:20]
        messages = [c.commit.message for c in recent_commits]

        # "Good" message heuristic: more than 3 words
        good_messages = sum(1 for m in messages if len(m.split()) > 3)
        
        ratio = good_messages / max(len(messages), 1)

        return {
            "total_commits": total_commits,
            "good_commit_ratio": ratio
        }
    except Exception:
        # Fallback if API fails or empty
        return {
            "total_commits": 0,
            "good_commit_ratio": 0
        }
