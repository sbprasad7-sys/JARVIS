import webbrowser


class WebsiteLauncher:

    def __init__(self):
        self.websites = {
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "chatgpt": "https://chatgpt.com",
            "google": "https://www.google.com",
            "gmail": "https://mail.google.com"
        }

    def open_website(self, name):
        name = name.lower().strip()

        if name in self.websites:
            print(f"🌐 Opening {name}...")
            webbrowser.open(self.websites[name])
            return True

        return False