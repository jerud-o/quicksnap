from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QFrame


class CustomMessageBox(QDialog):
    def __init__(self, message1, message2, image_path):
        super().__init__() # error: addition of dot between ) and _ 

        # Set window flags to remove title and close button
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # error: WA was removed

        # Set fixed size
        self.setFixedSize(700, 500)


        # Create QFrame to hold the message box contents
        frame = QFrame(self)
        frame.setStyleSheet("background-color: #fff; border-radius: 16px;") # error: " was removed

        # Create image label
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(250, 250)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create message label
        message_label1 = QLabel(message1)
        message_label1.setStyleSheet("color: #001D3D; font-size: 24px;font-weight: bold;") # error: color: was removed
        message_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create message label
        message_label2 = QLabel(message2)
        message_label2.setStyleSheet("color: #001D3D; font-size: 16px;font-weight: bold;")
        message_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create OK button
        ok_button = QPushButton("OK")
        ok_button.setFixedWidth(500);
        ok_button.setStyleSheet("background-color: #FFD50A; color: #001D3D; border-radius: 16px; padding: 10px; font-size: 18px;font-weight: bold;")
        ok_button.clicked.connect(self.accept)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget(message_label1)
        layout.addWidget(message_label2)
        layout.addWidget(ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
        frame.setLayout(layout)

        # Set frame layout on the dialog
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(frame, alignment=Qt.AlignmentFlag.AlignCenter)


app = QApplication([])
message1 = "Out Of Service"
message2 = "(photo paper or ink may be running low!)"
image_path = "package/resource/img/danger.png"
msg_box = CustomMessageBox(message1, message2, image_path)
msg_box.exec()
