import os
import time
from datetime import datetime
from shutil import get_terminal_size

FRAMES_FOLDER = "frames"
VERSION_FILE = "../config/version.wcode"
FRAME_DELAY = 0.05

# ASCII art logo for h-SHELL
ASCII_LOGO = [
    "                                                                               ",
    "                                                                               ",
    "  ,---,                               ,---,                  ,--,      ,--,    ",
    ",--.' |                             ,--.' |                ,--.'|    ,--.'|    ",
    "|  |  :         ,---,.              |  |  :                |  | :    |  | :    ",
    ":  :  :       ,'  .' |   .--.--.    :  :  :                :  : '    :  : '    ",
    ":  |  |,--. ,---.'   ,  /  /    '   :  |  |,--.    ,---.   |  ' |    |  ' |    ",
    "|  :  '   | |   |    | |  :  /`./   |  :  '   |   /     \\  '  | |    '  | |    ",
    "|  |   /' : :   :  .'  |  :  ;_     |  |   /' :  /    /  | |  | :    |  | :    ",
    "'  :  | | | :   |.'     \\  \\    `.  '  :  | | | .    ' / | '  : |__  '  : |__  ",
    "|  |  ' | : `---'        `----.   \\ |  |  ' | : '   ;   /| |  | '.'| |  | '.'| ",
    "|  :  :_:,'             /  /`--'  / |  :  :_:,' '   |  / | ;  :    ; ;  :    ; ",
    "|  | ,'                '--'.     /  |  | ,'     |   :    | |  ,   /  |  ,   /  ",
    "`--''                    `--'---'   `--''        \\   \\  /   ---`-'    ---`-'   ",
    "                                              `----'                          ",
    "                                                                               ",
]

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def load_version():
    try:
        with open(VERSION_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "v?.?.?"

def load_frames():
    frames = []
    files = sorted(os.listdir(FRAMES_FOLDER))
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(FRAMES_FOLDER, file), "r") as f:
                frame_lines = f.readlines()
                max_width = max(len(line.rstrip()) for line in frame_lines)
                frames.append((frame_lines, max_width))
    return frames

def display_animation():
    frames = load_frames()
    version = load_version()

    while True:
        term_width, term_height = get_terminal_size()

        for frame_lines, ascii_width in frames:
            clear_terminal()

            # Don't display if terminal is too narrow
            if term_width < ascii_width + 40:
                print(f"⛔ Terminal too small. Min width: {ascii_width + 40}")
                time.sleep(1)
                continue

            gap = 4  # space between ASCII and right panel
            right_start = ascii_width + gap
            right_width = term_width - right_start

            # Center the ASCII logo vertically in the right panel
            date_str = datetime.now().strftime("%Y-%m-%d")
            time_str = datetime.now().strftime("%H:%M:%S")
            right_content = ASCII_LOGO + ["", f"Version {version}", date_str, time_str]
            vertical_padding = max((term_height - len(right_content)) // 2, 0)

            # Render line by line
            for i in range(term_height):
                left = frame_lines[i].rstrip() if i < len(frame_lines) else ""
                left = left.ljust(ascii_width)
                right = ""

                # Display right content
                content_index = i - vertical_padding
                if 0 <= content_index < len(right_content):
                    right = right_content[content_index].center(right_width)
                else:
                    right = " " * right_width

                print(left + (" " * gap) + right)

            time.sleep(FRAME_DELAY)

if __name__ == "__main__":
    display_animation()
