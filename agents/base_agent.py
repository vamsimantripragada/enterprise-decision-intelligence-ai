from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    Ensures consistent interface across the system.
    """

    @abstractmethod
    def run(self, input_data: dict) -> dict:
        pass
