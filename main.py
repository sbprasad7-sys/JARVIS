from jarvis.brain import process


def main():
    print("=" * 40)
    print("        JARVIS INITIALIZED")
    print("=" * 40)

    while True:
        command = input("You: ").strip()

        if command.lower() == "exit":
            print("JARVIS: Goodbye!")
            break

        response = process(command)
        print(f"JARVIS: {response}")


if __name__ == "__main__":
    main()