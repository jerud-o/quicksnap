import cv2
import mediapipe as mp
from PyQt6.QtCore import QThread, pyqtSignal

class PalmDetectionThread(QThread):
    palm_detected = pyqtSignal(bool, str)

    def __init__(self, parent=None):
        super(PalmDetectionThread, self).__init__(parent)

        # MediaPipe's Configuration
        self.__mp_hands = mp.solutions.hands
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
            self.__results = self.__mp_hands.Hands().process(grayed_frame)

            if self.__results.multi_hand_landmarks:
                for hand_landmarks in self.__results.multi_hand_landmarks:
                    result = self.__get_fingertips_position(hand_landmarks)
                    self.draw_landmarks(frame, hand_landmarks)

                if result:
                    self.palm_detected.emit(True, "Palm Detected")
                    return
           
            self.palm_detected.emit(False, "No Palm Detected")

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

    def draw_landmarks(self, frame, hand_landmarks):
        if self.__draw_landmarks:
            self.__mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
