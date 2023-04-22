from PyQt6.QtCore import pyqtSignal, QThreadPool
from package.module.camera import CameraModule
from package.module.countdown_timer import CountdownTimerModule
from package.thread.palm import PalmDetectionThread
from package.thread.face import FaceDetectionThread
from package.thread.gaze import GazeEstimationThread


class QuickSnapCameraWidget(CameraModule, CountdownTimerModule):
    frame_captured = pyqtSignal(object)

    def __init__(self, mode):
        super().__init__()
        self.__process = self.__formal_process if mode == "formal" else self.__beauty_process
        self.__thread_pool = QThreadPool.globalInstance()
        self.__thread_pool.setMaxThreadCount(3)
        self.countdown_timer_finished.connect(self.__capture_frame)
        self.closeEvent = self.onCloseEvent

    def onCloseEvent(self, event):
        self.__stop_threads()
        super().closeEvent(event)

    def _process_frame(self):
        self.__process()
        self.__thread_pool.waitForDone()
        super()._process_frame()

    def __capture_frame(self):
        self.frame_captured.emit(self.frame_copy)

    def __formal_process(self):
        gaze_estimation = GazeEstimationThread()
        gaze_estimation.signals.frame_processed.connect(self.__update_frame_copy)
        gaze_estimation.signals.gaze_centered.connect(self._start_countdown_timer)

        face_detection = FaceDetectionThread(filter=True)
        face_detection.set_variables(self.frame_copy, self.frame_grayed)
        face_detection.signals.frame_processed.connect(gaze_estimation.start_service)
        
        self.__thread_pool.start(face_detection)
        self.__thread_pool.start(gaze_estimation)

    def __beauty_process(self):
        face_detection = FaceDetectionThread(filter=True)
        face_detection.set_variables(self.frame_copy, self.frame_grayed)

        palm_detection = PalmDetectionThread()
        palm_detection.set_variables(self.frame_copy, self.frame_grayed)
        palm_detection.signals.palm_detected.connect(self._start_countdown_timer)
        
        self.__thread_pool.start(face_detection)
        self.__thread_pool.start(palm_detection)

    def __update_frame_copy(self, frame_copy_new):
        self.frame_copy = frame_copy_new
