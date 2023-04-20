import cv2
import dlib
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal

class FaceDetectionThread(QThread):
    frame_processed = pyqtSignal(object, object)
    
    def __init__(self, parent=None):
        super(FaceDetectionThread, self).__init__(parent)
        
        # Dlib's Configuration
        self.__detector = dlib.get_frontal_face_detector()
        self.__predictor = dlib.shape_predictor("package/resource/shape_predictor_68_face_landmarks.dat")

        # Modifiable Variables
        self.__grayed_frame = None
        self.faces = None
        self.is_running = False

    def start(self, rectangle=False, landmarks=False):
        self.is_running = True
        self.__draw_rectangle = rectangle
        self.__draw_landmarks = landmarks
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()
    
    def process_frame(self, frame):
        if self.is_running:
            self.__grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR
            self.faces = self.__detector(self.__grayed_frame)
            self.draw_drawables(frame)

            # Emit signal with frame and detected faces
            self.frame_processed.emit(frame, self.faces)

    def get_landmarks(self, face):
        if self.__grayed_frame is not None:
            shape = self.__predictor(self.__grayed_frame, face)
            shape = self.convert_shape_to_numpy(shape)
            return shape

    def convert_shape_to_numpy(self, shape, dtype="int"):
        landmarks = np.zeros((68, 2), dtype=dtype)
        
        for i in range(0, 68):
            landmarks[i] = (shape.part(i).x, shape.part(i).y)
        
        return landmarks
    
    def draw_drawables(self, frame):
        if len(self.faces) > 0:
            for face in self.faces:
                if self.__draw_rectangle:
                    x = face.left()
                    y = face.top()
                    w = face.right() - x
                    h = face.bottom() - y
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if self.__draw_landmarks:
                    for (x, y) in self.get_landmarks(face):
                        cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

        
