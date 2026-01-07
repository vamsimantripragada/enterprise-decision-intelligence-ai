from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    def run(self, input_data: dict) -> dict:
        """
        Gathers information from web and documents.
        """
        return {
            "raw_findings": ["finding_placeholder"]
        }
