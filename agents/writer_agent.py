from agents.base_agent import BaseAgent
from agents.llm_client import LLMClient


class WriterAgent(BaseAgent):
    def __init__(self):
        self.llm = LLMClient()

    def run(self, input_data: dict) -> dict:
        findings = input_data.get("raw_findings", [])

        prompt = f"""
        You are an executive report writer.
        Using the findings below, write a concise executive summary
        and list 3–5 key findings.

        Findings:
        {findings}
        """

        response = self.llm.generate(prompt)

        lines = [l.strip() for l in response.split("\n") if l.strip()]
        summary = lines[0] if lines else ""
        key_findings = lines[1:6]

        return {
            "summary": summary,
            "key_findings": key_findings
        }
