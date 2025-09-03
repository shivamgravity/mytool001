import argparse

def main():
    parser = argparse.ArgumentParser(description="My first CLI tool")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
