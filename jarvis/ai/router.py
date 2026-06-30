from .local import LocalAI
from .cloud import CloudAI
from .exceptions import AIProviderError


class AIRouter:
    """
    Routes AI requests to the appropriate provider.
    """

    def __init__(self):
        self.local = LocalAI()
        self.cloud = CloudAI()

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the selected AI provider.
        """

        try:
            # For now, always use the local provider.
            return self.local.generate(prompt)

        except AIProviderError:
            # In the future we'll automatically switch to cloud AI.
            return self.cloud.generate(prompt)

        except Exception as e:
            return f"Unexpected AI error: {e}"