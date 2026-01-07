from agents.base_agent import BaseAgent
from agents.llm_client import LLMClient


class PlannerAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMClient()

    def run(self, input_data: dict) -> dict:
        query = input_data["query"]

        prompt = f"""
        You are an enterprise research planner.
        Break the following business question into clear research tasks:

        Question: {query}

        Return a bullet list of tasks.
        """

        response = self.llm.generate(prompt)

        tasks = [t.strip("- ").strip() for t in response.split("\n") if t.strip()]

        return {"tasks": tasks}
