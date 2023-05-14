from PyQt6.QtWidgets import QApplication
from package.app import App


# APPLICATION ENTRY POINT
if __name__ == '__main__':
    app = QApplication([])
    app_widget = App(app.arguments())
    app_widget.init_ui()
    app.exec()