from typing import TypedDict, List


class AgentState(TypedDict):
    query: str
    tasks: List[str]
    raw_findings: List[str]
    summary: str
    key_findings: List[str]
    confidence_score: float
