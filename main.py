from PyQt6.QtWidgets import QApplication
from package.app import App

if __name__ == '__main__':
    app = QApplication([])
    widget = App(app.arguments())
    widget.init_ui()
    app.exec()