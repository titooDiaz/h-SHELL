import os
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.wcode"

def parse_config():
    config = {}
    if not CONFIG_PATH.exists():
        print("Config file not found.")
        return config
    with open(CONFIG_PATH, "r") as file:
        for line in file:
            if "=" in line and not line.strip().startswith("#"):
                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()
    return config

def create_project_structure(name, config):
    base_path = Path(name)
    folders = ["src", "docs", "tests"]
    files = {
        "README.md": config.get("readme_text", "Project initialized."),
        ".gitignore": "*.pyc\n__pycache__/\n.env\n",
    }

    try:
        base_path.mkdir(exist_ok=False)
        print(f"✔ Created project folder: {name}")

        for folder in folders:
            (base_path / folder).mkdir()
            print(f"  └─ Created subfolder: {folder}")

        for filename, content in files.items():
            with open(base_path / filename, "w") as f:
                f.write(content + "\n")
            print(f"  └─ Created file: {filename}")

    except FileExistsError:
        print(f"✖ Project '{name}' already exists.")
    except Exception as e:
        print(f"✖ Error: {e}")

def run(args):
    if not args:
        print("Usage: generate-project <project_name>")
        return

    project_name = args[0]
    config = parse_config()
    create_project_structure(project_name, config)
