import os
import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage


class CameraModule(QLabel):
    def __init__(self):
        super().__init__()
        self.__capture = cv2.VideoCapture(int(os.environ.get('CAMERA_PORT')))

        self.setScaledContents(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def get_next_frame(self):
        ret, frame = self.__capture.read()

        if ret:
            print("new frame read")
            self.frame_copy = self.frame = frame
            self.frame_grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self._process_frame()
        
        # Schedule the next frame update
        QTimer.singleShot(int(1000 / int(os.environ.get('FRAME_RATE'))), self.get_next_frame)

    def _process_frame(self):
        self.setPixmap(QPixmap.fromImage(self.convert_frame_to_qimage(self.frame_copy)))

    def convert_frame_to_qimage(self, frame):
        # For preparing frames to be put into the QLabel
        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR

        h, w, ch = grayed_frame.shape
        bytes_per_line = ch * w
        
        # Conversion method
        image = QImage(grayed_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).mirrored(True, False)
        image = image.scaled(self.width(), int(self.width() * image.height() / image.width()), Qt.AspectRatioMode.KeepAspectRatio)
        return image