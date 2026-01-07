from langgraph.graph import StateGraph, END

from agents.state import AgentState
from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.validator_agent import ValidatorAgent
from agents.writer_agent import WriterAgent


def build_graph():
    planner = PlannerAgent()
    researcher = ResearchAgent()
    validator = ValidatorAgent()
    writer = WriterAgent()

    graph = StateGraph(AgentState)

    def planner_node(state: AgentState):
        output = planner.run({"query": state["query"]})
        state["tasks"] = output.get("tasks", [])
        return state

    def research_node(state: AgentState):
        output = researcher.run({"tasks": state.get("tasks", [])})
        state["raw_findings"] = output.get("raw_findings", [])
        return state

    def validator_node(state: AgentState):
        output = validator.run({"raw_findings": state.get("raw_findings", [])})
        state["confidence_score"] = output.get("confidence_score", 0.0)
        return state

    def writer_node(state: AgentState):
        output = writer.run(state)
        state["summary"] = output.get("summary", "")
        state["key_findings"] = output.get("key_findings", [])
        return state

    graph.add_node("planner", planner_node)
    graph.add_node("research", research_node)
    graph.add_node("validator", validator_node)
    graph.add_node("writer", writer_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "research")
    graph.add_edge("research", "validator")
    graph.add_edge("validator", "writer")
    graph.add_edge("writer", END)

    return graph.compile()
