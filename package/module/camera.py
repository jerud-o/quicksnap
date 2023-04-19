import os
import cv2
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage

class CameraModule():
    def __init__(self):
        super().__init__()
        self.__init_camera()

        # Frame Label
        self._frame_label = QLabel()
        self._frame_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        # Modifiable Variables
        self.__frame_size = QSize(640, 480)

    def __init_camera(self):
        self.__camera_port = int(os.environ.get('CAMERA_PORT'))
        self.__capture = cv2.VideoCapture(self.__camera_port)

    def get_next_frame(self):
        ret, frame = self.__capture.read()
        self._process_frame(ret, frame)
        
        # Schedule the next frame update
        QTimer.singleShot(1, self.get_next_frame)

    def _process_frame(self, ret, frame):
        if ret:
            self._show_frame(frame)

    def _show_frame(self, frame):
        image = self.convert_frame_to_qimage(frame)
        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def set_image_size(self, size):
        self.__frame_size = size

    def convert_frame_to_qimage(self, frame):
        # For preparing frames to be put into the QLabel
        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR

        h, w, ch = grayed_frame.shape
        bytes_per_line = ch * w
        
        # Conversion method
        image = QImage(grayed_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        image = image.scaled(self.__frame_size, Qt.AspectRatioMode.KeepAspectRatio)
        return image