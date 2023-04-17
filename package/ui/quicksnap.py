import cv2
from package.widget.camera import CameraWidget
from package.module.dlib import DlibModule
from package.module.face_detector import FaceDetectorModule
from package.module.gaze_tracker import GazeTrackerModule


class QuickSnapUI(CameraWidget):
    def __init__(self, camera_index=0, parent=None):
        super().__init__(camera_index, parent)
        self.dlib = DlibModule()
        self.face_detector = FaceDetectorModule()
        self.gaze_tracker = GazeTrackerModule()

    def process_frame(self, ret, frame):
        if ret:
            faces = self.dlib.get_detected_faces(frame)

            self.face_detector.set_frame(frame)
            self.gaze_tracker.set_frame(frame)

            if len(faces) > 0:
                for face in faces:
                    self.face_detector.set_face(face)
                    self.gaze_tracker.set_face(face)
                    self.gaze_tracker.get_gaze_position()
                    # FOR DEBUGGING
                    # self.face_detector.draw_rectangle()
                    # self.face_detector.draw_face_landmarks()

        super().process_frame(ret, frame)
