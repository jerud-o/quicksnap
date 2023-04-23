import numpy as np
import cv2
import mediapipe as mp

class HandDetectionModule():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.detector = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

        self.GLOW_SIGMA = 5
        self.GLOW_ALPHA = 0.5

        hand_landmark_dict = self.mp_hands.HandLandmark
        self.FINGERTIPS_IDS = [
            hand_landmark_dict.INDEX_FINGER_TIP,
            hand_landmark_dict.MIDDLE_FINGER_TIP,
            hand_landmark_dict.RING_FINGER_TIP,
            hand_landmark_dict.PINKY_TIP
        ]
        self.PALM_REGIONS_IDS = [
            hand_landmark_dict.WRIST,
            hand_landmark_dict.INDEX_FINGER_MCP,
            hand_landmark_dict.MIDDLE_FINGER_MCP,
            hand_landmark_dict.RING_FINGER_MCP,
            hand_landmark_dict.PINKY_MCP
        ]

    def process_frame(self, grayed_frame, mode, frame_to_show=None):
        grayed_frame.flags.writeable = False
        results = self.detector.process(grayed_frame)
        grayed_frame.flags.writeable = True
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            x, y = self.get_hand_center(hand_landmarks)
            if mode == 2: self.mp_draw.draw_landmarks(frame_to_show, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            gesture = self.identify_hand_gesture(hand_landmarks)
            return gesture, (x, y)

        return None, (-1, -1)
    
    def get_hand_center(self, hand_landmarks):
        x = y = 0
        num_landmarks = len(self.PALM_REGIONS_IDS)

        for landmark_index in self.PALM_REGIONS_IDS:
            x += hand_landmarks.landmark[landmark_index].x
            y += hand_landmarks.landmark[landmark_index].y

        x /= num_landmarks
        y /= num_landmarks
        return x, y

    def identify_hand_gesture(self, hand_landmarks):
        gesture = None
        is_fingertip_up = []

        for tip_index in self.FINGERTIPS_IDS:
            is_fingertip_up.append(hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y)
        
        if all(is_fingertip_up):
            gesture = "open"
        if not all(is_fingertip_up):
            gesture = "close"
        if all(is_fingertip_up[:2]) and not all(is_fingertip_up[2:]):
            gesture = "peace"

        # print(gesture)
        return gesture
