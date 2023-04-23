from package.vendor.gaze_tracking import GazeTracking
from PyQt6.QtCore import QThread, pyqtSignal


class GazeEstimationThread(QThread):
    frame_processed = pyqtSignal(object)
    gaze_centered = pyqtSignal()

    def __init__(self, parent=None):
        super(GazeEstimationThread, self).__init__(parent)
        self.__gaze_module = GazeTracking()

    def start(self, crosshairs=False):
        self.__draw_crosshairs = crosshairs
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()

    def set_variables(self, frame, frame_drawn, faces):
        self.__frame = frame
        self.__frame_drawn = frame_drawn
        self.__face = faces[0] if len(faces) > 0 else None

    def process_frame(self):
        if self.__face is not None:
            self.__gaze_module.refresh(self.__frame, self.__face)

            if self.__gaze_module.is_center():
                self.gaze_centered.emit()

            if self.__draw_crosshairs:
                frame = self.__gaze_module.annotated_frame()
                self.frame_processed.emit(frame)
