from automation.app_launcher import AppLauncher


class CommandRouter:
    def __init__(self):
        self.launcher = AppLauncher()

    def route(self, command: str):
        command = command.lower().strip()

        if command == "exit":
            return False

        if command.startswith("open "):
            app = command.replace("open ", "", 1)
            self.launcher.open_app(app)
            return True

        print("❌ I don't understand that command.")
        return True