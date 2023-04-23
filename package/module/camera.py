import os
import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage


class CameraModule(QLabel):
    frame = None
    frame_original = None

    def __init__(self):
        super().__init__()
        self.__init_camera()

        # self.setScaledContents(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("margin-top: 10px;")

    def __init_camera(self):
        self.__camera_port = int(os.environ.get('CAMERA_PORT'))
        self.__capture = cv2.VideoCapture(self.__camera_port)

    def get_next_frame(self):
        ret, frame = self.__capture.read()

        if ret:
            self.frame_drawn = self.frame = frame
            self.grayed_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR
            self._process_frame()
        
        # Schedule the next frame update
        QTimer.singleShot(1, self.get_next_frame)

    def _process_frame(self):
        self._show_frame()

    def _show_frame(self):
        self.setPixmap(QPixmap.fromImage(self.convert_frame_to_qimage()))

    def convert_frame_to_qimage(self):
        # For preparing frames to be put into the QLabel
        grayed_frame = cv2.cvtColor(self.frame_drawn, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR

        h, w, ch = grayed_frame.shape
        bytes_per_line = ch * w
        
        # Conversion method
        image = QImage(grayed_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).mirrored(True, False)
        # image = image.scaled(1280, 720, Qt.AspectRatioMode.KeepAspectRatio)
        return image