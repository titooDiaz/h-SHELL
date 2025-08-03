import sys
from commands import create_folder

COMMANDS = {
    "create-folder": create_folder,
}

def run():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        return

    COMMANDS[command].run(args)
