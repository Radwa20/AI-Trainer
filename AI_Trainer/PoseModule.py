import cv2
import mediapipe as mp
import time
import math
class poseDetector():
    def __init__(self, mode=False, upBody=False, modelComplex=1, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode= mode
        self.upBody= upBody
        self.modelComplex=modelComplex
        self.smooth= smooth
        
        self.detectionCon= detectionCon
        self.trackCon= trackCon
        self.mpDraw= mp.solutions.drawing_utils
        self.mpPose= mp.solutions.pose
        self.pose= self.mpPose.Pose(self.mode, self.upBody, self.modelComplex,self.smooth,
                                    self.detectionCon, self.trackCon)
        
    def findPose(self, img, draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results= self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        self.lmlist=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c =img.shape
                cx,cy= int(lm.x*w), int(lm.y*h)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy) ,5, (255,0,0), cv2.FILLED )
        return self.lmlist
    

def main():
    cap= cv2.VideoCapture('3.mp4')
    pTime=0
    detector= poseDetector()
    while True:
        success, img= cap.read()
        img= detector.findPose(img)
        lmlist= detector.findPosition(img)
        print(lmlist)
        cTime= time.time()
        fps=1/(cTime-pTime)
        pTime= cTime
        cv2.putText(img,str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3,
            (255,0,0) , 3)
        cv2.imshow('Image', img)
        cv2.waitKey(1)
        if (cv2.waitKey(1) & 0xFF) ==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
        
if __name__=="__main__":
    main()