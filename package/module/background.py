import os
import cv2
import numpy as np
from main import resource_path

class BackgroundModule():
    def __init__(self):
        self.LOWER_RANGE = np.array([0, 100, 0], dtype=np.uint8)
        self.UPPER_RANGE = np.array([100, 255, 100], dtype=np.uint8)
        self.background_image = None
        self.background_color = (255, 255, 255)

    def set_background(self, image_path):
        self.background_image = cv2.flip(cv2.imread(resource_path(image_path)), 1) if image_path else None

    def process_frame(self, frame):
        if self.background_image is None:
            background_value = np.zeros_like(frame)
            background_value[:] = self.background_color
        else:
            background_value = self.background_image = cv2.resize(self.background_image, (frame.shape[1], frame.shape[0]))

        mask = cv2.inRange(frame, self.LOWER_RANGE, self.UPPER_RANGE)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask_inverted = cv2.bitwise_not(mask)

        foreground = cv2.bitwise_and(frame, frame, mask=mask_inverted)
        background = cv2.bitwise_and(background_value, background_value, mask=mask)

        return cv2.add(foreground, background)
