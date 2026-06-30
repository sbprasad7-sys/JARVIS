import subprocess


def execute(command: str):
    command = command.lower().strip()

    apps = {
        "open notepad": "notepad",
        "open calculator": "calc",
        "open paint": "mspaint",
        "open cmd": "cmd",
        "open file explorer": "explorer",
    }

    if command in apps:
        subprocess.Popen(apps[command])
        return f"Opening {command.replace('open ', '').title()}..."

    return None