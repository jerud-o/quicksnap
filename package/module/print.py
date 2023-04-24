import os
import win32com.client as win32
from PyQt6.QtGui import QPixmap


class PrintModule():
    def __init__(self):
        self.ONE_INCH_POINTS = 72
        
        self.current_path = os.getcwd()
        self.temp_path = "package/resource/img/temp/"

    def start_service(self):
        self.word = win32.Dispatch("Word.Application")
        self.word.Visible = True

    def stop_service(self):
        self.word.Quit()

    def print(self, image, print_method):
        pixmap = QPixmap.fromImage(image)
        pixmap.save(self.temp_path + "image.png", "png")

        doc = self.word.Documents.Add()
        doc.PageSetup.PaperSize = 9
        cursor = doc.Range()

        match print_method:
            case 1:
                for y in range(2):
                    cursor.InsertBefore("\v")
                    self.insert_square_photo(cursor, 1, 4)
            
            case 2:
                for y in range(2):
                    cursor.InsertBefore("\v")
                    self.insert_square_photo(cursor, 2, 2)

            case 3:
                cursor.InsertBefore("\v")
                self.insert_square_photo(cursor, 1, 4)
                cursor.InsertBefore("\v")
                self.insert_square_photo(cursor, 2, 2)

            case 4:
                pass
            
            case 0:
                shape = cursor.InlineShapes.AddPicture(os.path.join(self.current_path, self.temp_path, "image.png"))
                shape.Width = self.ONE_INCH_POINTS * 6
                shape.Height = self.ONE_INCH_POINTS * 4
            
            case _:
                print("Invalid printing method")
                return
            
        doc.PrintOut()
        # doc.Close()

    def insert_square_photo(self, cursor, inches, num_of_photos):
        for x in range(num_of_photos):
            shape = cursor.InlineShapes.AddPicture(os.path.join(self.current_path, self.temp_path, "image.png"))
            shape.Width = shape.Height = self.ONE_INCH_POINTS * inches