class AIProviderError(Exception):
    """
    Base exception for all AI-related errors.
    """
    pass


class OllamaNotRunning(AIProviderError):
    """
    Raised when Ollama is not running or cannot be reached.
    """
    pass


class CloudAPIError(AIProviderError):
    """
    Raised when the cloud AI provider returns an error.
    """
    pass