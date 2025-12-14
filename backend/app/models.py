from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class RepoRequest(BaseModel):
    url: str

class ScoreBreakdown(BaseModel):
    code_quality: int
    structure: int
    docs: int
    tests: int
    git: int
    relevance: int

class AnalysisResult(BaseModel):
    repo_name: str
    owner: str
    score: int
    breakdown: ScoreBreakdown
    summary: str
    roadmap: List[str]
    metadata: Dict[str, Any]
    details: Dict[str, Any]
