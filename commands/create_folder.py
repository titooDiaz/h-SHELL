import os

def run(args):
    """
    Creates a directory with the given name.
    Usage: create-folder <folder_name>
    """
    folder_name = args[0] if args else None
    if not folder_name:
        print("Error: You must provide a folder name.")
        return
    
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"✔ Folder '{folder_name}' created successfully.")
    except Exception as e:
        print(f"✖ Error creating folder: {e}")
