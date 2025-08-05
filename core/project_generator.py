import os
from pathlib import Path
from core.config_parser import load_main_config
from core.structure_parser import load_structure

def replace_vars(content, vars_dict):
    for key, val in vars_dict.items():
        content = content.replace(f"{{{key}}}", val)
    return content

def generate_project(name):
    meta_config = load_main_config()["meta"]
    folders, files = load_structure()

    project_path = Path(name)
    if project_path.exists():
        print(f"✖ Project '{name}' already exists.")
        return

    meta = dict(meta_config)
    meta["project_name"] = name

    project_path.mkdir()
    print(f"✔ Created project folder: {name}")

    for folder in folders:
        folder_path = project_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  └─ Created folder: {folder}")

    for file_name, raw_content in files.items():
        content = replace_vars(raw_content, meta)
        with open(project_path / file_name, "w") as f:
            f.write(content + "\n")
        print(f"  └─ Created file: {file_name}")
