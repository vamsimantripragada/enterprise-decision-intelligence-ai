from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.validator_agent import ValidatorAgent
from agents.writer_agent import WriterAgent


class Orchestrator:
    """
    Coordinates execution of all AI agents.
    This will later be replaced/enhanced with LangGraph.
    """

    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.validator = ValidatorAgent()
        self.writer = WriterAgent()

    def run(self, query: str) -> dict:
        # Step 1: Planning
        plan_output = self.planner.run({"query": query})

        # Step 2: Research
        research_output = self.researcher.run(plan_output)

        # Step 3: Validation
        validation_output = self.validator.run(research_output)

        # Step 4: Writing
        report_output = self.writer.run({
            "research": research_output,
            "validation": validation_output
        })

        return {
            "summary": report_output.get("summary"),
            "key_findings": report_output.get("key_findings"),
            "confidence_score": validation_output.get("confidence_score"),
        }
