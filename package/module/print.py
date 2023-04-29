import os
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import inch
from PyQt6.QtGui import QPixmap, QTransform

class PrintModule():
    def __init__(self):
        self.PAGE_WIDTH, self.PAGE_HEIGHT = 4 * inch, 6 * inch
        self.IMAGE_PATH = os.path.join(os.getcwd(), "package/resource/img/temp/img.png")

    def print(self, image, print_method):
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.transformed(QTransform().rotate(90))
        pixmap.save(self.IMAGE_PATH)

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
            c = canvas.Canvas(temp_file.name, pagesize=portrait((self.PAGE_WIDTH, self.PAGE_HEIGHT)))
            
            match print_method:
                case 1:
                    cursor_x = 0

                    for x in range(2):
                        cursor_y = 0
                        
                        for y in range(4):
                            c.drawImage(self.IMAGE_PATH, cursor_x, cursor_y, width=1*inch, height=1*inch)
                            cursor_y += 1 * inch

                        cursor_x += 1 * inch
                
                case 2:
                    cursor_x = 0

                    for x in range(2):
                        cursor_y = 0
                        
                        for y in range(2):
                            c.drawImage(self.IMAGE_PATH, cursor_x, cursor_y, width=2*inch, height=2*inch)
                            cursor_y += 2 * inch

                        cursor_x += 2 * inch

                case 3:
                    cursor_x = 0
                    cursor_y = 0

                    for y in range(4):
                        c.drawImage(self.IMAGE_PATH, cursor_x, cursor_y, width=1*inch, height=1*inch)
                        cursor_y += 1 * inch

                    cursor_x += 1 * inch
                    cursor_y = 0

                    for y in range(2):
                        c.drawImage(self.IMAGE_PATH, cursor_x, cursor_y, width=2*inch, height=2*inch)
                        cursor_y += 2 * inch
                
                case 0:
                    c.drawImage(self.IMAGE_PATH, 0, 0, width=4*inch, height=6*inch)
                
                case _:
                    print("Invalid printing method")
                    return

            c.showPage()
            c.save()
            os.startfile(temp_file.name)
            # os.startfile(temp_file.name, "print")
            