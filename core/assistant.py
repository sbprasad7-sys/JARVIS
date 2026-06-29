from core.command_router import CommandRouter
from core.parser import CommandParser

class Jarvis:
    def __init__(self):
        self.version = "MARK-0 v0.2"
        self.router = CommandRouter()
        self.parser = CommandParser()

    def start(self):
        print("=" * 50)
        print("🤖 JARVIS INITIALIZED")
        print(f"Version : {self.version}")
        print("Status  : ONLINE")
        print("=" * 50)

        while True:
            command = input("\nJARVIS > ")

            parsed_command = self.parser.parse(command)

            keep_running = self.router.route(parsed_command)

            if not keep_running:
                print("👋 Goodbye!")
                break