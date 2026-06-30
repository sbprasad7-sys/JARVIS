from datetime import datetime


def process(command: str) -> str:
    command = command.lower().strip()

    if command == "hello":
        return "Hello! How can I help you?"

    elif command == "who are you":
        return "I am JARVIS, your personal AI assistant."

    elif command == "time":
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    elif command == "date":
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    elif command == "help":
        return (
            "Try these commands:\n"
            "- hello\n"
            "- who are you\n"
            "- time\n"
            "- date\n"
            "- help\n"
            "- exit"
        )

    else:
        return "Sorry, I don't understand that command yet."