import sys
from core.command_loader import get_command_aliases

def run():
    command_map = get_command_aliases()

    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command not in command_map:
        print(f"Unknown command: {command}")
        return

    command_map[command].run(args)
