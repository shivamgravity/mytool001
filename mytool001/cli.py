import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool that greets the user.")
    parser.add_argument("name", nargs="?", help="Your name")
    parser.add_argument("time", nargs="?", help="Morning/AfterNoon/Evening/Night")
    args = parser.parse_args()

    # If no name is passed, ask interactively
    name = args.name or input("Enter your name: ")
    time = args.time or input("Enter the time of day (Morning/AfterNoon/Evening/Night): ")
    print(f"Hello, {name}! Good {time}.")
