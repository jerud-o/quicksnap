import numpy as np
import cv2
import dlib


class DlibModule():
    def __init__(self):
        self.init_dlib()

    # private
    def init_dlib(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("package/resource/shape_predictor_68_face_landmarks.dat")

    # protected
    def set_frame(self, frame):
        self.frame = frame
        self.set_frame_grayed(frame)

    # private
    def set_frame_grayed(self, frame):
        self.frame_grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # protected
    def get_face_landmarks(self, face):
        shape = self.predictor(self.frame_grayed, face)
        shape = self.shape_to_np(shape)
        return shape
    
    # public
    def shape_to_np(self, shape, dtype="int"):
        coords = np.zeros((68, 2), dtype=dtype)
        for i in range(0, 68):
            coords[i] = (shape.part(i).x, shape.part(i).y)
        return coords
    
    # public
    def get_detected_faces(self, frame=None):
        self.set_frame_grayed(frame)
        return self.detector(self.frame_grayed)
    