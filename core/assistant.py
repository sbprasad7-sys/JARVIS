from core.command_router import CommandRouter


class Jarvis:
    def __init__(self):
        self.version = "MARK-0 v0.2"
        self.router = CommandRouter()

    def start(self):
        print("=" * 50)
        print("🤖 JARVIS INITIALIZED")
        print(f"Version : {self.version}")
        print("Status  : ONLINE")
        print("=" * 50)

        while True:
            command = input("\nJARVIS > ")

            keep_running = self.router.route(command)

            if not keep_running:
                print("👋 Goodbye!")
                break