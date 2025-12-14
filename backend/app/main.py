from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import os

from app.github_fetcher import fetch_repo_data
from app.code_analyzer import analyze_code
from app.commit_analyzer import analyze_commits
from app.scoring_engine import calculate_score, get_level
from app.ai_summary import generate_summary
from app.roadmap import generate_roadmap
from app.pdf_generator import generate_pdf
from pydantic import BaseModel

app = FastAPI(title="GitGrade AI", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: str

@app.post("/analyze")
def analyze_repo_endpoint(request: AnalyzeRequest):
    import sys
    try:
        repo_url = request.url.strip()
        print(f"DEBUG: Received Request for URL: {repo_url}", file=sys.stderr, flush=True)
        
        # Basic URL fix
        if not repo_url.startswith("https://") and not repo_url.startswith("http://"):
            repo_url = "https://" + repo_url
        
        # 1. Fetch
        print(f"DEBUG: Fetching data for: {repo_url}", file=sys.stderr, flush=True)
        repo_data = fetch_repo_data(repo_url)
        
        if "error" in repo_data:
            print(f"DEBUG: Error fetching repo: {repo_data['error']}", file=sys.stderr, flush=True)
            raise HTTPException(status_code=400, detail=f"GitHub API Error: {repo_data['error']}")
    except Exception as e:
        print(f"DEBUG: Exception in analyze endpoint: {str(e)}", file=sys.stderr, flush=True)
        raise HTTPException(status_code=400, detail=f"Server Analysis Error: {str(e)}")

    # 2. Analyze
    code_metrics = analyze_code(repo_data)
    commit_metrics = analyze_commits(repo_url)

    # 3. Score
    score = calculate_score(code_metrics, commit_metrics, repo_data)
    level = get_level(score)

    # 4. Generate
    summary = generate_summary(repo_data, code_metrics, commit_metrics)
    roadmap = generate_roadmap(score, code_metrics, commit_metrics)

    # 5. PDF (Optional generation here or on demand)
    # let's generic it here to have it ready? Or separate endpoint. 
    # Final Spec calls for download endpoint but let's return path or ID.
    
    return {
        "repo_name": repo_data["name"],
        "owner": repo_url.split('/')[-2], # heuristic
        "score": score,
        "level": level,
        "summary": summary,
        "roadmap": roadmap,
        "details": {
            "code": code_metrics,
            "commits": commit_metrics
        }
    }

@app.get("/download-pdf")
def download_pdf_endpoint(repo: str, score: int, summary: str, roadmap: str):
    # Re-generating PDF on the fly or saving it.
    # Passing complex data via GET is bad. Better to use POST or pass ID.
    # For simplicity of hackathon, let's accept params or re-analyze. 
    # Or cleaner: The frontend sends the data to generate PDF.
    
    # Let's parse roadmap list from string (comma sep) for this simple demo
    roadmap_list = roadmap.split(',')
    
    path = generate_pdf(repo, score, summary, roadmap_list)
    return FileResponse(path, media_type='application/pdf', filename=os.path.basename(path))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
