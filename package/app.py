from PyQt6.QtWidgets import QApplication, QMainWindow
from dotenv import load_dotenv
from package.ui.widget.main import MainWidget


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        load_dotenv()
    
    def init_ui(self):
        self.main_window = QMainWindow()
        main_widget = MainWidget()
        self.main_window.setCentralWidget(main_widget)
        self.main_window.show()
