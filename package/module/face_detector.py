import cv2
from package.module.dlib import DlibModule


class FaceDetectorModule(DlibModule):
    def __init__(self):
        super().__init__()

    # public
    def set_face(self, face):
        self.face = face

    # public
    def draw_rectangle(self):
        x = self.face.left()
        y = self.face.top()
        w = self.face.right() - x
        h = self.face.bottom() - y
        cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # public
    def draw_face_landmarks(self):
        for (x, y) in self.get_face_landmarks(self.face):
            cv2.circle(self.frame, (x, y), 2, (0, 0, 255), -1)
