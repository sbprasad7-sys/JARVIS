from .base import AIProvider


class CloudAI(AIProvider):
    """
    Cloud AI provider.
    This will later connect to OpenAI or another cloud API.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the cloud AI model.
        """
        return "Cloud AI placeholder"