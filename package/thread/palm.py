import cv2
import mediapipe as mp
from PyQt6.QtCore import QThread, pyqtSignal

class PalmDetectionThread(QThread):
    palm_detected = pyqtSignal(bool, str)

    def __init__(self, parent=None):
        super(PalmDetectionThread, self).__init__(parent)

        # MediaPipe's Configuration
        self.__mp_hands = mp.solutions.hands.Hands()
        self.__mp_draw = mp.solutions.drawing_utils

        # Modifiable Variables
        self.__results = None
        self.is_running = False
    
    def start(self, landmarks=False):
        self.is_running = True
        self.__draw_landmarks = landmarks
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()
                        
    def process_frame(self, frame):
        if self.is_running:
            grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR
            self.__results = self.__mp_hands.process(grayed_frame)

            if self.__results.multi_hand_landmarks:
                self.draw_landmarks(frame)
                self.palm_detected.emit(True, "Palm Detected")
            else:
                self.palm_detected.emit(False, "No Palm Detected")

    def draw_landmarks(self, frame):
        if self.__draw_landmarks:
            for hand_landmarks in self.__results.multi_hand_landmarks:
                self.__mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
