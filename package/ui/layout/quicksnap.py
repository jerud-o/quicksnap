from PyQt6.QtWidgets import QWidget, QVBoxLayout
from package.ui.widget.quicksnap_camera import QuickSnapCameraWidget


class QuickSnapLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        widget = QuickSnapCameraWidget()
        
        layout = QVBoxLayout()
        layout.addWidget(widget)
        
        self.setLayout(layout)