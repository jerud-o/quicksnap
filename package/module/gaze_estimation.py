import cv2
import dlib
import numpy as np


class GazeEstimationModule():
    def __init__(self):
        self.init_dlib()

    def init_dlib(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("package/resource/shape_predictor_68_face_landmarks.dat")

    def set_params(self, frame, face):
        self.frame = frame
        self.face = face

    def get_gaze_direction(self):
        landmarks = self.get_landmarks()

        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        

    def draw_rectangle(self):
        x = self.face.left()
        y = self.face.top()
        w = self.face.right() - x
        h = self.face.bottom() - y
        cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def get_landmarks(self):
        shape = self.predictor(self.frame, self.face)
        return [(shape.part(i).x, shape.part(i).y) for i in range(1, 68)]
