from jarvis.commands.system import execute as system_execute
from jarvis.commands.web import execute as web_execute
from jarvis.commands.apps import execute as apps_execute

from jarvis.ai.router import AIRouter


# Create one AI router instance
ai_router = AIRouter()


def process(command: str) -> str:
    command = command.strip()

    # First try all built-in commands
    for handler in (
        system_execute,
        apps_execute,
        web_execute,
    ):
        response = handler(command)
        if response:
            return response

    # If no command matches, ask the AI
    return ai_router.generate(command)