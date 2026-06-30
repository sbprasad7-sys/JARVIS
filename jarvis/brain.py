from jarvis.commands.system import execute as system_execute
from jarvis.commands.web import execute as web_execute
from jarvis.commands.apps import execute as apps_execute


def process(command: str) -> str:
    command = command.strip()

    for handler in (
        system_execute,
        apps_execute,
        web_execute,
    ):
        response = handler(command)
        if response:
            return response

    return "Sorry, I don't understand that command yet."