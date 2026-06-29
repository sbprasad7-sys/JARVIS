class CommandParser:

    def __init__(self):
        # Different words that mean "open"
        self.open_words = [
            "open",
            "launch",
            "start",
            "run"
        ]

        # Words we want to ignore
        self.ignore_words = [
            "please",
            "can",
            "could",
            "would",
            "you",
            "jarvis"
        ]

    def parse(self, command):

        command = command.lower().strip()

        words = command.split()

        # Remove filler words
        words = [word for word in words if word not in self.ignore_words]

        # Replace synonyms with "open"
        normalized = []

        for word in words:
            if word in self.open_words:
                normalized.append("open")
            else:
                normalized.append(word)

        return " ".join(normalized)
        print(f"[DEBUG] Parsed command: {parsed}")
        return parsed