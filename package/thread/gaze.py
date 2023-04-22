from package.vendor.gaze_tracking import GazeTracking
from PyQt6.QtCore import QObject, QRunnable, pyqtSignal


class GazeEstimationSignals(QObject):
    frame_processed = pyqtSignal(object)
    gaze_centered = pyqtSignal()


class GazeEstimationThread(QRunnable):
    def __init__(self, crosshairs=False):
        super().__init__()
        self.signals = GazeEstimationSignals()
        self.__draw_crosshairs = crosshairs
        self.__gaze_module = GazeTracking()

    def run():
        pass

    def start_service(self, frame_copy, face):
        if face:
            self.__frame_copy = frame_copy
            self.__gaze_module.refresh(self.__frame_copy, face)
            self.draw_drawables()
            if self.__gaze_module.is_center(): self.signals.gaze_centered.emit()
            self.signals.frame_processed.emit(self.__frame_copy)

    def draw_drawables(self):
        if self.__draw_crosshairs:
            self.__frame_copy = self.__gaze_module.annotated_frame()
                
                    
            
