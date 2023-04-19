from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a QVBoxLayout to hold the widgets vertically
        layout = QVBoxLayout()
        
        # Create a QPushButton and add it to the layout
        button1 = QPushButton('Button 1')
        layout.addWidget(button1)
        
        # Create another QPushButton and add it to the layout
        button2 = QPushButton('Button 2')
        layout.addWidget(button2)
        
        # Set the widget's layout
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
