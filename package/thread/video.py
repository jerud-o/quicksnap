import os
import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition, Qt, QSize
from PyQt6.QtGui import QImage


class VideoThread(QThread):
    frame_ready = pyqtSignal(np.ndarray)
    error = pyqtSignal(str)

    MAX_QUEUE_SIZE = 10

    def __init__(self, parent=None):
        super(VideoThread, self).__init__(parent)
        
        # VideoCapture's Configuration
        self.__camera_port = int(os.environ.get('CAMERA_PORT'))
        self.__capture = cv2.VideoCapture(self.__camera_port)

        # Queueing Variales
        self.__queue_lock = QMutex()
        self.__queue_not_full = QWaitCondition()
        self.__queue = []

        # Modifiable Variables
        self.__frame_size = QSize(640, 480)
        self.is_running = False
    
    def start(self):
        self.is_running = True
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()

    def run(self):
        # Error Handling: Camera Port
        if not self.__capture.isOpened():
            self.error.emit("Failed to open video capture device")
            return

        while self.is_running:
            ret, frame = self.__capture.read()

            # Error Handling: VideoCapture Frame
            if not ret:
                self.error.emit("Failed to capture frame from video stream")
                break
            
            self.frame_ready.emit(frame)

        self.__capture.release()

    def set_image_size(self, size):
        # For window resizing
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