from agents.base_agent import BaseAgent
from agents.llm_client import LLMClient
from rag.rag_service import RAGService


class ResearchAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMClient()
        self.rag = RAGService()

    def run(self, input_data: dict) -> dict:
        tasks = input_data.get("tasks", [])

        context = self.rag.retrieve_context(" ".join(tasks))

        prompt = f"""
        You are an enterprise research analyst.
        Use ONLY the context below to answer.

        Context:
        {context}

        Tasks:
        {tasks}

        Provide factual bullet-point findings.
        """

        response = self.llm.generate(prompt)

        findings = [f.strip("- ").strip() for f in response.split("\n") if f.strip()]

        return {"raw_findings": findings}
