import cv2
import mediapipe as mp
from PyQt6.QtCore import QThread, pyqtSignal

class PalmDetectionThread(QThread):
    palm_detected = pyqtSignal()

    def __init__(self, parent=None):
        super(PalmDetectionThread, self).__init__(parent)

        # MediaPipe's Configuration
        self.__mp_hands = mp.solutions.hands
        self.__mp_draw = mp.solutions.drawing_utils
    
    def start(self, landmarks=False):
        self.__draw_landmarks = landmarks
        super().start()

    def stop(self):
        self.terminate()
    
    def set_variables(self, frame_drawn, grayed_frame):
        self.__frame_drawn = frame_drawn
        self.__grayed_frame = grayed_frame
    
    def process_frame(self):
        results = self.__mp_hands.Hands().process(self.__grayed_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                result = self.__get_fingertips_position(hand_landmarks)
                self.draw_landmarks(hand_landmarks)

            if result: self.palm_detected.emit()

    def __get_fingertips_position(self, hand_landmarks):
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

    def draw_landmarks(self, hand_landmarks):
        if self.__draw_landmarks:
            self.__mp_draw.draw_landmarks(self.__frame_drawn, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
