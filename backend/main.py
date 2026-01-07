from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from agents.graph import build_graph
graph = build_graph()


from schemas import ResearchRequest, ResearchResponse
from agents.orchestrator import Orchestrator

app = FastAPI
(
    title="Enterprise Decision Intelligence AI Platform (EDIP)",
    version="1.0.0"
)

app.add_middleware
(
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
    initial_state = 
    {
        "query": request.query,
        "tasks": [],
        "raw_findings": [],
        "summary": "",
        "key_findings": [],
        "confidence_score": 0.0
    }

    final_state = graph.invoke(initial_state)

    return ResearchResponse
    (
        report_id=str(uuid4()),
        summary=final_state["summary"],
        key_findings=final_state["key_findings"],
        sources=request.sources,
        confidence_score=final_state["confidence_score"]
    )
