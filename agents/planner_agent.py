from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):
    def run(self, input_data: dict) -> dict:
        """
        Breaks a business query into structured research tasks.
        """
        return {
            "tasks": ["task_1_placeholder", "task_2_placeholder"]
        }
