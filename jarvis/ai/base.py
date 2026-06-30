from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Base class for all AI providers.
    Every provider (Ollama, OpenAI, etc.) must inherit from this class.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the AI model.
        """
        pass