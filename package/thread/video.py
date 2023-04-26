import os
import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal
from package.module.hand import HandDetectionModule
from package.module.face import FaceDetectionModule
from package.module.gaze import GazeDetectionModule
from package.module.background import BackgroundModule


class VideoThread(QThread):
    capture_gesture_detected = pyqtSignal()
    frame_ready = pyqtSignal(tuple)
    mode = 0

    def __init__(self):
        super().__init__()
        self.__init_camera()
        self.__init_modules()
        self.is_running = False
        self.is_capturing = False

    def __init_camera(self):
        self.__camera_port = int(os.environ.get('CAMERA_PORT'))
        self.__capture = cv2.VideoCapture(self.__camera_port)

    def __init_modules(self):
        self.hand_module = HandDetectionModule()
        self.face_module = FaceDetectionModule()
        self.gaze_module = GazeDetectionModule()
        self.background_module = BackgroundModule()

    def run(self):
        self.is_running = True
        
        while self.is_running:
            ret, frame = self.__capture.read()

            if ret:
                grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                if self.mode != 0:
                    frame = self.background_module.process_frame(frame)
                    frame_to_show = np.copy(frame)
                    frame_to_print = np.copy(frame)
                    
                    if self.mode == 2 and not self.is_capturing:
                        if self.hand_module.process_frame(grayed_frame, self.mode, frame_to_show):
                            self.capture_gesture_detected.emit()

                    self.process_frame(frame, grayed_frame, frame_to_show, frame_to_print)
                    self.frame_ready.emit((frame_to_show, frame_to_print))
                else:
                    self.hand_module.process_frame(grayed_frame, self.mode)
                
    def stop(self):
        self.is_running = False
        self.terminate()

    def set_is_capturing(self, is_capturing):
        self.is_capturing = is_capturing

    def set_mode(self, mode):
        self.mode = mode

        match self.mode:
            case 1: self.process_frame = self.formal_process
            case 2: self.process_frame = self.beauty_process
            case _: self.process_frame = self.null_process

    def formal_process(self, frame, grayed_frame, frame_to_show, frame_to_print):
        self.face_module.process_frame(grayed_frame, frame_to_show, frame_to_print)

        if len(self.face_module.faces) > 0 and not self.is_capturing:
            is_looking_center = self.gaze_module.process_frame(grayed_frame, self.face_module.faces[0])
            if is_looking_center: self.capture_gesture_detected.emit()

    def beauty_process(self, frame, grayed_frame, frame_to_show, frame_to_print):
        self.face_module.process_frame(grayed_frame, frame_to_show, frame_to_print)

    def null_process(*_):
        pass
    