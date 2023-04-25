import os
import cv2
import numpy as np
import pyautogui
from PyQt6.QtCore import QThread, pyqtSignal
from package.module.face import FaceDetectionModule
from package.module.gaze import GazeDetectionModule
from package.module.hand import HandDetectionModule


class VideoThread(QThread):
    capture_gesture_detected = pyqtSignal()
    frame_ready = pyqtSignal(tuple)
    mode = 0

    def __init__(self):
        super().__init__()
        self.__init_camera()
        self.__init_modules()
        pyautogui.FAILSAFE = False
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pyautogui.size()
        self.SCREEN_WIDTH *= 1.2
        self.SCREEN_HEIGHT *= 1.2
        self.is_running = False

    def __init_camera(self):
        self.__camera_port = int(os.environ.get('CAMERA_PORT'))
        self.__capture = cv2.VideoCapture(self.__camera_port)

    def __init_modules(self):
        self.face_module = FaceDetectionModule()
        self.gaze_module = GazeDetectionModule()
        self.hand_module = HandDetectionModule()

    def run(self):
        self.is_running = True
        
        while self.is_running:
            ret, frame = self.__capture.read()

            if ret:
                grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                if self.mode != 0:
                    frame_to_show = np.copy(frame)
                    frame_to_print = np.copy(frame)                    
                    hand_gesture, hand_center_coords = self.hand_module.process_frame(grayed_frame, self.mode, frame_to_show)
                    self.process_frame(grayed_frame, frame_to_show, frame_to_print)
                    self.frame_ready.emit((frame_to_show, frame_to_print))
                else:
                    hand_gesture, hand_center_coords = self.hand_module.process_frame(grayed_frame, self.mode)

                self.handle_hand_location(hand_center_coords)
                self.handle_hand_gesture(hand_gesture)
                
    def stop(self):
        self.is_running = False
        self.terminate()

    def handle_hand_location(self, hand_center_coords):
        x, y = hand_center_coords

        if x >= 0 and y >= 0:
            new_x = self.SCREEN_WIDTH - int(x * self.SCREEN_WIDTH)
            new_y = self.SCREEN_HEIGHT - int((1 - y) * self.SCREEN_HEIGHT)
            pyautogui.moveTo(new_x, new_y)

    def handle_hand_gesture(self, hand_gesture):
        match hand_gesture:
            case "open":
                pyautogui.mouseUp()

            case "close":
                pyautogui.mouseDown()
            
            case "peace":
                if self.mode == 2:
                    self.capture_gesture_detected.emit()

    def set_mode(self, mode):
        self.mode = mode

        match self.mode:
            case 1: self.process_frame = self.formal_process
            case 2: self.process_frame = self.beauty_process
            case _: self.process_frame = self.null_process

    def formal_process(self, grayed_frame, frame_to_show, frame_to_print):
        self.face_module.process_frame(grayed_frame, frame_to_show, frame_to_print)

        if len(self.face_module.faces) > 0:
            is_looking_center = self.gaze_module.process_frame(grayed_frame, self.face_module.faces[0])
            if is_looking_center: self.capture_gesture_detected.emit()

    def beauty_process(self, grayed_frame, frame_to_show, frame_to_print):
        self.face_module.process_frame(grayed_frame, frame_to_show, frame_to_print)

    def null_process(*_):
        pass
    