import os
import time

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def play_ascii_frames(directory="frames", fps=24):
    files = sorted(os.listdir(directory))
    delay = 1 / fps

    for file in files:
        with open(os.path.join(directory, file)) as f:
            content = f.read()
        clear_terminal()
        print(content)
        time.sleep(delay)