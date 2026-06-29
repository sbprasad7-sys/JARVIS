import subprocess


class AppLauncher:

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
            print(f"Sorry, I don't know how to open '{app_name}'.")