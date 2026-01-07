from agents.base_agent import BaseAgent
from agents.llm_client import LLMClient


class ResearchAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMClient()

    def run(self, input_data: dict) -> dict:
        tasks = input_data.get("tasks", [])

        prompt = f"""
        You are a research analyst.
        For the following tasks, provide concise factual findings:

        Tasks:
        {tasks}

        Provide short bullet-point findings.
        """

        response = self.llm.generate(prompt)

        findings = [f.strip("- ").strip() for f in response.split("\n") if f.strip()]

        return {"raw_findings": findings}
