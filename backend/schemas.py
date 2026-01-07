from pydantic import BaseModel
from typing import List, Optional


class ResearchRequest(BaseModel):
    query: str
    sources: Optional[List[str]] = ["web", "documents"]
    depth: Optional[str] = "standard"


class ResearchResponse(BaseModel):
    report_id: str
    summary: str
    key_findings: List[str]
    sources: List[str]
    confidence_score: float
