from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from package.module.camera import CameraModule
from package.thread.palm import PalmDetectionThread
from package.thread.face import FaceDetectionThread
from package.thread.gaze import GazeEstimationThread


class QuickSnapCameraWidget(QWidget, CameraModule):
    countdown_timer = pyqtSignal(str)
    frame_captured = pyqtSignal(object)

    def __init__(self, parent=None):
        super(QuickSnapCameraWidget, self).__init__(parent)

        # Thread Declarations
        self.__palm_thread = PalmDetectionThread()
        self.__face_thread = FaceDetectionThread()
        self.__gaze_thread = GazeEstimationThread()

        # Connect signals to threads
        self.__palm_thread.palm_detected.connect(self.__start_timer)
        # self.__gaze_thread.gaze_centered.connect(self.__start_timer)
        self.__gaze_thread.frame_processed.connect(super()._process_frame)

        # Timer Variables
        self.__TIMER_DURATION = 3
        self.__time_left = self.__TIMER_DURATION
        self.__timer = QTimer(timeout=self.__update_timer)

        self.closeEvent = self.onCloseEvent
        self.__init_ui()

    # def resizeEvent(self, event):
    #     super(QuickSnapCameraWidget, self).resizeEvent(event)

    #     # Updates camera thread's config for proper QImage rendering
    #     self.set_image_size(self.size())

    def onCloseEvent(self, event):
        self.__stop_threads()
        super().closeEvent(event)

    def __init_ui(self):
        # QuickSnap's Camera Widget Layout
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self._frame_label)
        self.setMinimumSize(640, 480)
        self.setLayout(self.__layout)

    def start_threads(self):
        self.__palm_thread.start()
        self.__face_thread.start(filter=True)
        self.__gaze_thread.start()

    def stop_threads(self):
        self.__palm_thread.stop()
        self.__face_thread.stop()
        self.__gaze_thread.stop()

    def _process_frame(self):
        # Wait for threads to finish before showing the frame
        if self.frame is not None:
            self.__palm_thread.process_frame(self.frame)
            self.__face_thread.process_frame(self.frame)
            # self.__gaze_thread.process_frame(self.frame, self.__face_thread.faces)

    def __capture_frame(self):
        self.frame_captured.emit(self.frame)

    def __start_timer(self, is_start, signal_str):
        if not self.__timer.isActive() and is_start:
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
