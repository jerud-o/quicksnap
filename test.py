import os
import win32com.client as win32
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QImage, QPixmap

# Constants
image_location = "package/resource/img/man.png"
temp_path = "package/resource/img/temp/"
current_path = os.getcwd()
ONE_INCH_POINTS = 72

# Qt 
app = QApplication([])
qimage = QImage(image_location)
qpixmap = QPixmap.fromImage(qimage)
qpixmap.save(temp_path + "formal.png", "png")

# Word Instance
word = win32.Dispatch("Word.Application")
word.Visible = True

# Word Variables
doc = word.Documents.Add()
cursor = doc.Range()

# Picture Insertion
package = "D"

match package:
    case "A":
        for y in range(2):
            cursor.InsertBefore("\v")

            for x in range(4):
                shape = cursor.InlineShapes.AddPicture(os.path.join(current_path, temp_path, "formal.png"))
                shape.Width = shape.Height = ONE_INCH_POINTS
    
    case "C":
        for y in range(2):
            cursor.InsertBefore("\v")

            for x in range(2):
                shape = cursor.InlineShapes.AddPicture(os.path.join(current_path, temp_path, "formal.png"))
                shape.Width = shape.Height = ONE_INCH_POINTS * 2
    
    case "D":
        cursor.InsertBefore("\v")

        for x in range(4):
            shape = cursor.InlineShapes.AddPicture(os.path.join(current_path, temp_path, "formal.png"))
            shape.Width = shape.Height = ONE_INCH_POINTS

        cursor.InsertBefore("\v")

        for x in range(2):
            shape = cursor.InlineShapes.AddPicture(os.path.join(current_path, temp_path, "formal.png"))
            shape.Width = shape.Height = ONE_INCH_POINTS * 2
    
    case "beauty":
        pass

    case _:
        print("Package not found")
