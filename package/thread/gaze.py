import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal

class GazeEstimationThread(QThread):
    frame_processed = pyqtSignal(object, object)

    def __init__(self, parent=None):
        super(GazeEstimationThread, self).__init__(parent)
        
        # Constant Variables
        self.__KERNEL = np.ones((9, 9), np.uint8)
        self.__THRESHOLD = 66
        self.__LEFT_EYE_INDICES = list(range(36, 42))
        self.__RIGHT_EYE_INDICES = list(range(42, 48))
        self.__CROSSHAIR_RADIUS = 5

        # Modifiable Variable
        # WARNING: self.__irises_centroids might get overwritten sooner
        #          than expected since only one instance of this thread
        #          is started
        self.__irises_centroids = np.empty((2, 2))

    def start(self):
        self.is_running = True
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()

    def process_frame(self, frame, face_thread):
        faces = face_thread.faces

        if self.is_running:
            if len(faces) > 0:
                temp = []

                for face in faces:
                    landmarks = face_thread.get_landmarks(face)
                    eyes_grayed = self.__create_mask_on_eyes(frame, landmarks)
                    irises = self.__isolate_iris(eyes_grayed)
                    eyes_midpoint = (landmarks[39][0] + landmarks[42][0]) // 2
                    left_iris_centroid = self.__contour_eye(irises, eyes_midpoint)
                    right_iris_centroid = self.__contour_eye(irises, eyes_midpoint, right=True)

                    if left_iris_centroid is not None and right_iris_centroid is not None:
                        temp.append([left_iris_centroid, right_iris_centroid])

                self.__irises_centroids = np.array(temp)
                print(temp)

            self.frame_processed.emit(frame, self.__irises_centroids)

    def __create_mask_on_eyes(self, frame, landmarks):
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        mask = self.__create_eye_mask(mask, landmarks, self.__LEFT_EYE_INDICES)
        mask = self.__create_eye_mask(mask, landmarks, self.__RIGHT_EYE_INDICES)
        mask = cv2.dilate(mask, self.__KERNEL, 5)
        eyes = cv2.bitwise_and(frame, frame, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        return cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
    
    def __create_eye_mask(self, mask, landmarks, eye_landmarks):
        eye_points = [landmarks[i] for i in eye_landmarks]
        eye_points = np.array(eye_points, dtype=np.int32)
        mask = cv2.fillConvexPoly(mask, eye_points, 255)
        return mask
    
    def __isolate_iris(self, eyes):
        _, thresh = cv2.threshold(eyes, self.__THRESHOLD, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2) # Filter 1
        thresh = cv2.dilate(thresh, None, iterations=4) # Filter 2
        thresh = cv2.medianBlur(thresh, 3) # Filter 3
        thresh = cv2.bitwise_not(thresh)
        return thresh
    
    def __contour_eye(self, thresh, eyes_midpoint, right=False):
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        try:
            cnt = max(cnts, key = cv2.contourArea)
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            
            if right:
                cx += eyes_midpoint

            return (cx, cy)
        except:
            return None

    def draw_drawables(self, frame, crosshairs=False, circles=False):
        RAD = self.__CROSSHAIR_RADIUS
        
        if self.__irises_centroids.size:
            pass
            # for left_iris, right_iris in (self.__irises_centroids):
            #     left_x, left_y = left_iris, right_iris
            #     right_x, right_y = right_iris, left_iris

            #     if crosshairs:
            #         left_points = {
            #             'hx': (int(left_x - RAD), int(left_y)),
            #             'hy': (int(left_x + RAD), int(left_y)),
            #             'vx': (int(left_x), int(left_y - RAD)),
            #             'vy': (int(left_x), int(left_y + RAD))
            #         }
            #         right_points = {
            #             'hx': (int(right_x - RAD), int(right_y)),
            #             'hy': (int(right_x + RAD), int(right_y)),
            #             'vx': (int(right_x), int(right_y - RAD)),
            #             'vy': (int(right_x), int(right_y + RAD))
            #         }

            #         cv2.line(frame, left_points['hx'], left_points['hy'], (0, 0, 255), 1)
            #         cv2.line(frame, left_points['vx'], left_points['vy'], (0, 0, 255), 1)
            #         cv2.line(frame, right_points['hx'], right_points['hy'], (0, 0, 255), 1)
            #         cv2.line(frame, right_points['vx'], right_points['vy'], (0, 0, 255), 1)

            #     if circles:
            #         # cv2.circle(frame, left_iris, 4, (0, 0, 255), 1)
            #         # cv2.circle(frame, right_iris, 4, (0, 0, 255), 1)
            #         pass
