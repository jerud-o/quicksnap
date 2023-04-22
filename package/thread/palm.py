import cv2
import mediapipe as mp
from PyQt6.QtCore import QObject, QRunnable, pyqtSignal


class PalmDetectionSignals(QObject):
    palm_detected = pyqtSignal()


class PalmDetectionThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = PalmDetectionSignals()

        # MediaPipe's Configuration
        self.__mp_hands = mp.solutions.hands
        self.__mp_draw = mp.solutions.drawing_utils

    def set_variables(self, frame_copy, frame_grayed, landmarks=False):
        self.__frame_copy = frame_copy
        self.__frame_grayed = frame_grayed
        self.__draw_landmarks = landmarks

    def run(self):
        self.__results = self.__mp_hands.Hands().process(self.__frame_grayed)
        
        if self.__results.multi_hand_landmarks:
            for hand_landmarks in self.__results.multi_hand_landmarks:
                result = self.__is_palm_open(hand_landmarks)
                self.draw_landmarks(hand_landmarks)
                
                if result:
                    self.signals.palm_detected.emit()
                    break

    def __is_palm_open(self, hand_landmarks):
        hand_landmark_dict = self.__mp_hands.HandLandmark
        fingertips_ids = [
            hand_landmark_dict.INDEX_FINGER_TIP,
            hand_landmark_dict.MIDDLE_FINGER_TIP,
            hand_landmark_dict.RING_FINGER_TIP,
            hand_landmark_dict.PINKY_TIP
        ]
        is_up = True

        for tip_index in fingertips_ids:
            if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y):
                continue
            else:
                is_up = False
                break

        return is_up

    def draw_drawables(self, hand_landmarks):
        if self.__draw_landmarks:
            self.__mp_draw.draw_landmarks(self.__frame_copy, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)