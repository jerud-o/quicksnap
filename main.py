import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# APPLICATION ENTRY POINT
if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    from package.app import App

    app = QApplication([])
    app_widget = App(app.arguments())
    app_widget.init_ui()
    app.exec()