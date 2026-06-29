import subprocess
from automation.browser import WebsiteLauncher


class AppLauncher:

    def __init__(self):
        self.website_launcher = WebsiteLauncher()

    def open_app(self, app_name):
        app_name = app_name.lower()

        apps = {
            "chrome": "chrome",
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "cmd": "cmd"
        }

        if app_name in apps:
            print(f"Opening {app_name}...")
            subprocess.Popen(apps[app_name])
        else:
            if not self.website_launcher.open_website(app_name):
                print(f"Sorry, I don't know how to open '{app_name}'.")