from PyQt6.QtWidgets import QApplication, QMainWindow
from dotenv import load_dotenv
from package.ui.widget.main import MainWidget


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        load_dotenv()
    
    def init_ui(self):
        self.main_window = QMainWindow()
        
        self.main_widget = MainWidget(self.main_window)
        self.main_widget.exit_app_btn.clicked.connect(self.exit_app)
        
        self.main_window.showFullScreen()
        self.main_widget.video_thread.start()
        self.main_window.show()

    def exit_app(self):
        self.main_widget.video_thread.stop()
        self.main_window.close()
