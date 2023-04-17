from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from package.ui.quicksnap import QuickSnapUI

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

    def init_ui(self):
        self.main_window = QMainWindow()
        widget = QuickSnapUI(camera_index=0)
        QTimer.singleShot(1, widget.get_next_frame)
        self.main_window.setCentralWidget(widget)
        self.main_window.show()