import cv2
import os

ASCII_CHARS = "█▓▒░ ."

def resize_frame(frame, width):
    height, original_width = frame.shape
    aspect_ratio = height / float(original_width)
    new_height = int(aspect_ratio * width * 0.55)
    return cv2.resize(frame, (width, new_height))

def gray_to_ascii(image):
    ascii_frame = ""

    for row in image:
        for pixel in row:
            index = int(pixel) * len(ASCII_CHARS) // 256
            ascii_frame += ASCII_CHARS[index]
        ascii_frame += "\n"

    return ascii_frame

def generate_ascii_frames(video_path, output_dir="frames", width=100):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        inverted = 255 - gray
        resized = resize_frame(inverted, width)
        ascii_frame = gray_to_ascii(resized)

        with open(f"{output_dir}/frame_{count:05d}.txt", "w") as f:
            f.write(ascii_frame)

        count += 1

    cap.release()
    print(f"✅ {count} frames in .txt")
