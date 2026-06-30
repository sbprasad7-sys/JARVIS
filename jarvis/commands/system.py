from datetime import datetime


def execute(command: str):
    command = command.lower()

    if command == "time":
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    if command == "date":
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    if command == "who are you":
        return "I am JARVIS, your personal AI assistant."

    if command == "hello":
        return "Hello! How can I help you?"

    return None