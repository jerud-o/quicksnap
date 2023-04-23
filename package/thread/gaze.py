from package.vendor.gaze_tracking import GazeTracking
from PyQt6.QtCore import QThread, pyqtSignal


class GazeEstimationThread(QThread):
    frame_processed = pyqtSignal(bool, object)
    gaze_centered = pyqtSignal(bool, str)

    def __init__(self, parent=None):
        super(GazeEstimationThread, self).__init__(parent)

        # Gaze Tracking Library
        self.__gaze_module = GazeTracking()

    def start(self, crosshairs=False):
        self.is_running = True
        self.__draw_crosshairs = crosshairs
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()

    def process_frame(self, frame, faces):
        if self.is_running:
            if len(faces) > 0:
                face = faces[0]
                
                self.__gaze_module.refresh(frame, face)

                if self.__gaze_module.is_center():
                    self.gaze_centered.emit(True, "Gaze centered")

                if self.__draw_crosshairs:
                    frame = self.__gaze_module.annotated_frame()
                    
            self.frame_processed.emit(True, frame)
