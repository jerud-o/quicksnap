import pyautogui
import mediapipe as mp

class HandDetectionModule():
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.detector = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

        self.FINGERTIPS_IDS = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]

        pyautogui.FAILSAFE = False
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pyautogui.size()

    def process_frame(self, grayed_frame, mode, frame_to_show=None):
        results = self.detector.process(grayed_frame)
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            self.handle_hand_location(self.get_hand_center(hand_landmarks))
            
            if mode == 2 and frame_to_show is not None:
                self.mp_draw.draw_landmarks(frame_to_show, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
            return self.manage_hand_gesture(hand_landmarks)

        return False

    def handle_hand_location(self, hand_center_coords):
        x, y = hand_center_coords

        new_x = self.SCREEN_WIDTH - int((x * self.SCREEN_WIDTH))
        new_y = self.SCREEN_HEIGHT - int((1 - y) * self.SCREEN_HEIGHT)
        pyautogui.moveTo(new_x, new_y)
    
    def get_hand_center(self, hand_landmarks):
        return ((hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x, hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y))

    def manage_hand_gesture(self, hand_landmarks):
        is_fingertip_up = []

        for tip_index in self.FINGERTIPS_IDS:
            is_fingertip_up.append(hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y)
        
        if is_fingertip_up[0] and all(x is False for x in is_fingertip_up[1:]):
            pyautogui.mouseUp()
        elif all(x is False for x in is_fingertip_up):
            pyautogui.mouseDown()
        elif all(is_fingertip_up[:2]) and all(x is False for x in is_fingertip_up[2:]):
            return True

        return False
