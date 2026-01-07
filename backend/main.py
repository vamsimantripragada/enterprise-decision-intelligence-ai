from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4

from schemas import ResearchRequest, ResearchResponse
from agents.orchestrator import Orchestrator

app = FastAPI(
    title="Enterprise Decision Intelligence AI Platform (EDIP)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "EDIP Backend"}


@app.post("/research", response_model=ResearchResponse)
def run_research(request: ResearchRequest):
    result = orchestrator.run(request.query)

    return ResearchResponse(
        report_id=str(uuid4()),
        summary=result["summary"],
        key_findings=result["key_findings"],
        sources=request.sources,
        confidence_score=result["confidence_score"]
    )
