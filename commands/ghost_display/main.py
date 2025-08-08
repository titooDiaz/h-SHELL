from .frame_generator import generate_ascii_frames
#from .ascii_player import play_ascii_frames
from .display import display_animation

# you can change the name of the file
import os
video_path = os.path.join(os.path.dirname(__file__), "video.mp4")
frames_dir = os.path.join(os.path.dirname(__file__), "../../frames")
frame_width = 100
fps = 60

def run(args):
    os.makedirs(frames_dir, exist_ok=True)

    # Verificar si ya existen frames .txt
    txt_frames = [f for f in os.listdir(frames_dir) if f.endswith(".txt")]

    if not txt_frames:
        print("[INFO] No frames found. Generating from video...")
        generate_ascii_frames(video_path, width=frame_width)
    else:
        print(f"[INFO] {len(txt_frames)} frames found. Skipping generation.")

    print("[INFO] Starting animation...")
    display_animation()