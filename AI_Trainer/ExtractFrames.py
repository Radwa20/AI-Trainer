import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    frame_count = 0
    success = True

    while success:
        success, frame = cap.read()
        if success:
            if frame_count % frame_rate == 0:
                frame_path = os.path.join(output_folder, f"9_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
extract_frames("C:/Users/20109/OneDrive/Desktop/New-Coach/OutVideo/9.mp4", "C:/Users/20109/OneDrive/Desktop/New-Coach/val/downward_facing_dog", frame_rate=5)
