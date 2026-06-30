from .base import AIProvider


class LocalAI(AIProvider):
    """
    Local AI provider.
    This will later connect to Ollama.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the local AI model.
        """
        return "Local AI placeholder"