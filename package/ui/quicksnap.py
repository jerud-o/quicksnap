import cv2
from package.widget.camera import CameraWidget
from package.module.gaze_estimation import GazeEstimationModule


class QuickSnapUI(CameraWidget):
    def __init__(self, camera_index=0, parent=None):
        super().__init__(camera_index, parent)
        self.gaze_estimation = GazeEstimationModule()

    def process_frame(self, ret, frame):
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.gaze_estimation.detector(gray)

            if len(faces) > 0:
                for face in faces:
                    self.gaze_estimation.set_params(frame, face)
                    self.gaze_estimation.draw_rectangle()
                    self.gaze_estimation.get_gaze_direction()

        super().process_frame(ret, frame)
