from PyQt6.QtWidgets import QWidget, QStackedLayout
from package.ui.layout.quicksnap import QuickSnapLayout


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        # All application's layout declaration
        # TODO: Create multiple layouts
        quicksnap_layout = QuickSnapLayout()

        stacked_layout = QStackedLayout()
        # TODO: add all layouts to stacked_layout
        stacked_layout.addWidget(quicksnap_layout)
        stacked_layout.setCurrentIndex(0)

        # TODO: connect each buttons with slot

        self.setLayout(stacked_layout)