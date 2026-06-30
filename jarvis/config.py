from dataclasses import dataclass
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()


@dataclass
class Settings:
    # Local AI (Ollama)
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    LOCAL_MODEL: str = os.getenv("LOCAL_MODEL", "llama3")

    # Cloud AI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    CLOUD_MODEL: str = os.getenv("CLOUD_MODEL", "gpt-4.1-mini")


# Create one global settings object
settings = Settings()