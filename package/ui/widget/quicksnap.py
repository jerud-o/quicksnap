import cv2
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage


class QuickSnapWidget(QLabel):
    def __init__(self, parent=None):
        super(QuickSnapWidget, self).__init__(parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_shown_frame(self, frame):
        self.setPixmap(QPixmap.fromImage(self.convert_frame_to_qimage(frame)))

    def convert_frame_to_qimage(self, frame):
        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = grayed_frame.shape
        bytes_per_line = ch * w
        
        # Conversion method
        image = QImage(grayed_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).mirrored(True, False)
        return image