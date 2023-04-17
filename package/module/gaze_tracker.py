import cv2
import numpy as np
from package.module.dlib import DlibModule


class GazeTrackerModule(DlibModule):
    def __init__(self):
        super().__init__()

    # public
    def set_face(self, face):
        self.face = face

    # private
    def create_eye_mask(self, mask, eye_landmarks):
        eye_points = [self.landmarks[i] for i in eye_landmarks]
        eye_points = np.array(eye_points, dtype=np.int32)
        mask = cv2.fillConvexPoly(mask, eye_points, 255)
        return mask

    def contouring(self, thresh, mid, img, right=False):
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        try:
            cnt = max(cnts, key = cv2.contourArea)
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            if right:
                cx += mid
            cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
        except:
            pass

    # public
    def get_gaze_position(self):
        self.landmarks = self.get_face_landmarks(self.face)
        left_eye_indices = list(range(36, 42))
        right_eye_indices = list(range(42, 48))

        mask = np.zeros(self.frame.shape[:2], dtype=np.uint8)
        mask = self.create_eye_mask(mask, left_eye_indices)
        mask = self.create_eye_mask(mask, right_eye_indices)
        mask = cv2.dilate(mask, np.ones((9, 9), np.uint8), 5)
        eyes = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        mid = (self.landmarks[42][0] + self.landmarks[39][0]) // 2
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
        threshold = 66
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) #1
        thresh = cv2.dilate(thresh, None, iterations=4) #2
        thresh = cv2.medianBlur(thresh, 3) #3
        thresh = cv2.bitwise_not(thresh)
        self.contouring(thresh[:, 0:mid], mid, self.frame)
        self.contouring(thresh[:, mid:], mid, self.frame, True)
