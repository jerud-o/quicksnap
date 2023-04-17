from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import cv2


class CameraWidget(QtWidgets.QWidget):
    def __init__(self, camera_index=0, parent=None):
        super().__init__(parent)
        self.camera_index = camera_index
        self.init_ui()
        self.init_camera()

    def init_ui(self):
        self.setWindowTitle("Camera Widget")
        self.camera_label = QtWidgets.QLabel()
        self.camera_label.setFixedSize(640, 480)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.camera_label)
        self.setLayout(layout)

    def init_camera(self):
        self.capture = cv2.VideoCapture(self.camera_index)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def process_frame(self, ret, frame):
        if ret:
            self.camera_label.setPixmap(self.convert_frame_to_img(frame))

    def convert_frame_to_img(self, frame):
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        frame_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        frame_img = frame_img.rgbSwapped()
        return QtGui.QPixmap.fromImage(frame_img)

    def get_next_frame(self):
        ret, frame = self.capture.read()
        self.process_frame(ret, frame)
        # Schedule the next frame update
        QtCore.QTimer.singleShot(1, self.get_next_frame)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = CameraWidget()
    widget.show()
    QtCore.QTimer.singleShot(1, widget.get_next_frame)
    sys.exit(app.exec())