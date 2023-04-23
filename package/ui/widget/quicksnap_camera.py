from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from package.module.camera import CameraModule
from package.thread.palm import PalmDetectionThread
from package.thread.face import FaceDetectionThread
from package.thread.gaze import GazeEstimationThread


class QuickSnapCameraWidget(CameraModule):
    countdown_timer = pyqtSignal(str)
    frame_captured = pyqtSignal(object)

    def __init__(self, mode, parent=None):
        super().__init__()
        self.__mode = mode
        self.__process = self.__formal_process if self.__mode == "formal" else self.__beauty_process 
        # Thread Declarations
        self.__palm_thread = PalmDetectionThread()
        self.__face_thread = FaceDetectionThread()
        self.__gaze_thread = GazeEstimationThread()

        # Connect signals to threads
        self.__palm_thread.palm_detected.connect(self.start_timer)
        self.__gaze_thread.frame_processed.connect(self.__update_frame_drawn)
        self.__gaze_thread.gaze_centered.connect(self.start_timer)

        # Timer Variables
        self.__TIMER_DURATION = 3
        self.__time_left = self.__TIMER_DURATION
        self.__timer = QTimer(timeout=self.__update_timer)

        self.closeEvent = self.onCloseEvent

    def onCloseEvent(self, event):
        self.__stop_threads()
        super().closeEvent(event)

    def start_threads(self):
        if self.__mode == "formal":
            self.__face_thread.start()
            self.__gaze_thread.start()
        else:
            self.__palm_thread.start()
            self.__face_thread.start(filter=True)

    def stop_threads(self):
        if self.__mode == "formal":
            self.__face_thread.stop()
            self.__gaze_thread.stop()
        else:
            self.__palm_thread.stop()
            self.__face_thread.stop()

    def __update_frame_drawn(self, new_frame):
        self.frame_drawn = new_frame

    def _process_frame(self):
        self.__process()
        super()._process_frame()
            
    def __formal_process(self):
        self.__face_thread.set_variables(self.frame_drawn, self.grayed_frame)
        self.__face_thread.process_frame()
        self.__gaze_thread.set_variables(self.frame, self.frame_drawn, self.__face_thread.faces)
        self.__gaze_thread.process_frame()

    def __beauty_process(self):
        self.__palm_thread.set_variables(self.frame_drawn, self.grayed_frame)
        self.__palm_thread.process_frame()
        self.__face_thread.set_variables(self.frame_drawn, self.grayed_frame)
        self.__face_thread.process_frame()

    def __capture_frame(self):
        self.frame_captured.emit(self.frame)

    def start_timer(self):
        if not self.__timer.isActive():
            self.__timer.start(1000)
            self.countdown_timer.emit(str(self.__time_left))

    def __stop_timer(self):
        self.__timer.stop()
        self.countdown_timer.emit("")
        self.__time_left = self.__TIMER_DURATION

    def __update_timer(self):
        self.__time_left -= 1

        self.countdown_timer.emit(str(self.__time_left))

        if self.__time_left == 0:
            self.__stop_timer()
            self.__capture_frame()
