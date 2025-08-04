import sys
from commands import create_folder

from commands import create_folder, generate_project

COMMANDS = {
    "create-folder": create_folder,
    "generate-project": generate_project,
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
