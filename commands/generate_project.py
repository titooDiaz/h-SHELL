from core.project_generator import generate_project

def run(args):
    if not args:
        print("Usage: <command> <project_name>")
        return
    generate_project(args[0])
