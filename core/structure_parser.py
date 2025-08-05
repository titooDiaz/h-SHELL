from pathlib import Path

STRUCTURE_PATH = Path(__file__).parents[1] / "config" / "project_structure.wcode"

def load_structure():
    folders = []
    files = {}

    with open(STRUCTURE_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(">"):
                folders.append(line[1:].strip())
            elif "=" in line:
                file, content = line.split("=", 1)
                files[file.strip()] = content.strip()
    
    return folders, files
