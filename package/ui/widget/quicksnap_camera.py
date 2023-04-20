from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from package.module.camera import CameraModule
from package.thread.palm import PalmDetectionThread
from package.thread.face import FaceDetectionThread
from package.thread.gaze import GazeEstimationThread


class QuickSnapCameraWidget(QWidget, CameraModule):
    def __init__(self, parent=None):
        super(QuickSnapCameraWidget, self).__init__(parent)

        # Thread Declarations
        self.__palm_thread = PalmDetectionThread()
        self.__face_thread = FaceDetectionThread()
        self.__gaze_thread = GazeEstimationThread()

        # Connect signals to threads
        self.__palm_thread.palm_detected.connect(self.__start_timer)
        self.__gaze_thread.gaze_centered.connect(self.__start_timer)
        self.__gaze_thread.frame_processed.connect(super()._process_frame)

        # Start Service
        self.__start_threads()
        QTimer.singleShot(1, self.get_next_frame)

        self.closeEvent = self.onCloseEvent
        self.__init_ui()

    def resizeEvent(self, event):
        super(QuickSnapCameraWidget, self).resizeEvent(event)

        # Updates camera thread's config for proper QImage rendering
        self.set_image_size(self.size())

    def onCloseEvent(self, event):
        self.__stop_threads()
        super().closeEvent(event)

    def __init_ui(self):
        # QuickSnap's Camera Widget Layout
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self._frame_label)
        self.setMinimumSize(640, 480)
        self.setLayout(self.__layout)

    def __start_threads(self):
        self.__palm_thread.start()
        self.__face_thread.start()
        self.__gaze_thread.start()

    def __stop_threads(self):
        self.__palm_thread.stop()
        self.__face_thread.stop()
        self.__gaze_thread.stop()

    def _process_frame(self, ret, frame):
        # Wait for threads to finish before showing the frame
        self.__palm_thread.process_frame(frame)
        self.__face_thread.process_frame(frame)
        self.__gaze_thread.process_frame(frame, self.__face_thread.faces)

    def __start_timer(self):
        # Start timer thread, updating the QLabel
        # Once done, call a function "capture"
        pass
