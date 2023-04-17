import sys
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
import dlib

class GazeEstimationWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the UI
        self.camera_label = QtWidgets.QLabel()
        self.camera_label.setFixedSize(640, 480)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.camera_label)
        self.setLayout(layout)

        # Set up the camera
        self.capture = cv2.VideoCapture(1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Set up the face detector and shape predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def get_gaze_direction(self, image):
        # Detect faces in the image
        faces = self.detector(image)

        # Check if at least one face is detected
        if len(faces) > 0:
            # Draw a rectangle around each detected face
            for face in faces:
                x = face.left()
                y = face.top()
                w = face.right() - x
                h = face.bottom() - y
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Get the landmarks for the first face
            shape = self.predictor(image, faces[0])
            landmarks = [(shape.part(i).x, shape.part(i).y) for i in range(1, 68)]

            # Estimate the gaze direction using the eye landmarks
            left_eye = landmarks[36:42]
            right_eye = landmarks[42:48]
            # your gaze estimation code here

    def next_frame(self):
        # Get the next frame from the camera
        ret, frame = self.capture.read()

        # Process the frame
        if ret:
            # Detect faces in the frame
            faces = self.detector(frame)

            # Estimate the gaze direction
            gaze_direction = self.get_gaze_direction(frame)

            # Convert the OpenCV frame to a QImage
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qImg = qImg.rgbSwapped()

            # Set the QImage as the pixmap of the camera label
            self.camera_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

        # Schedule the next frame update
        QtCore.QTimer.singleShot(1, self.next_frame)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = GazeEstimationWidget()
    widget.show()
    QtCore.QTimer.singleShot(1, widget.next_frame)
    sys.exit(app.exec())
