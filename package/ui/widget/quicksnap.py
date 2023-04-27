import cv2
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage


class QuickSnapWidget(QLabel):
    def __init__(self, parent=None):
        super(QuickSnapWidget, self).__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_shown_frame(self, frame):
        self.setPixmap(QPixmap.fromImage(frame))

    def convert_frame_to_qimage(self, frame, mode):
        h, w, _ = frame.shape

        if mode == 1:
            x = int((w - h) / 2)
            y = 0
            frame = frame[y:y+h, x:x+h]
        elif mode == 2:
            w = int(h * (3 / 2))
            x = int((w - w) / 2)
            y = 0
            frame = frame[y:y+h, x:x+w]

        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = grayed_frame.shape
        bytes_per_line = ch * w

        image = QImage(grayed_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).mirrored(True, False)

        return image