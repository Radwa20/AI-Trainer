import mediapipe as mp
import numpy as np
import cv2
import time
import os
import PoseModule as pm

input_folder = "C:/Users/20109/OneDrive/Desktop/AI_Coach/tt"  
output_folder = "C:/Users/20109/OneDrive/Desktop/AI_Coach/out"  



def process_images_in_folder(input_folder, output_folder):
    detector = pm.poseDetector()
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"): 
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            img = detector.findPose(img)
            lmlist = detector.findPosition(img)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, img)
process_images_in_folder(input_folder, output_folder)
