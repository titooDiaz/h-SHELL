from frame_generator import generate_ascii_frames
from ascii_player import play_ascii_frames

# you can change the name of the file
video_path = "video.mp4"
frame_width = 100
fps = 60

generate_ascii_frames(video_path, width=frame_width)
play_ascii_frames(fps=fps)