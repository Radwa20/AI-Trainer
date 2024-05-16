import cv2
import os
from PoseModule import poseDetector

input_video_path = "C:/Users/20109/OneDrive/Desktop/New-Coach/val/3.mp4"
output_video_folder = "C:/Users/20109/OneDrive/Desktop/New-Coach/OutVideo"
output_video_path = os.path.join(output_video_folder, "5.mp4")

def process_video(input_video_path, output_video_path):
    if not os.path.exists(output_video_folder):
        os.makedirs(output_video_folder)

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Could not open input video.")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    if not out.isOpened():
        print("Error: Could not open output video for writing.")
        return

    detector = poseDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = detector.findPose(frame)
        lm_list = detector.findPosition(frame)

        out.write(frame)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Processing complete. Output saved to: {output_video_path}")

process_video(input_video_path, output_video_path)
