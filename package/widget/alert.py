from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QColor, QPen
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton


class CustomMessageBox(QDialog):
    def __init__(self, message, image_path):
        super().__init__()

        # Set window flags to remove title and close button
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Set fixed size
        self.setFixedSize(700, 500)

        # Set border-radius
        self.setStyleSheet("background-color: #fff; border: 2px solid #001D3D; border-radius: 10px;")

        # Create message label
        message_label = QLabel(message)
        message_label.setStyleSheet(
            "color: #001D3D;font-size: 18px;font-weight: bold;")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create image label
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(250, 250)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create OK button
        ok_button = QPushButton("OK")
        ok_button.setFixedWidth(500)
        ok_button.setStyleSheet("background-color: #FFD50A; color: #001D3D; border-radius: 10px; padding: 10px; font-size: 18px;font-weight: bold;")
        ok_button.clicked.connect(self.accept)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget(message_label)
        layout.addWidget(ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


app = QApplication([])
message = "Photo Paper or Ink is running low!"
image_path = "package/resource/img/danger.png"
msg_box = CustomMessageBox(message, image_path)
msg_box.exec()
