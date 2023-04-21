import cv2
import dlib
import numpy as np
from math import hypot
from PyQt6.QtCore import QThread, pyqtSignal

class FaceDetectionThread(QThread):
    frame_processed = pyqtSignal(object, object)
    
    def __init__(self, parent=None):
        super(FaceDetectionThread, self).__init__(parent)
        
        # Dlib's Configuration
        self.__detector = dlib.get_frontal_face_detector()
        self.__predictor = dlib.shape_predictor("package/resource/shape_predictor_68_face_landmarks.dat")

        # Modifiable Variables
        self.__grayed_frame = None
        self.faces = None
        self.is_running = False

    def start(self, rectangle=False, landmarks=False, filter=False):
        self.is_running = True
        self.__draw_rectangle = rectangle
        self.__draw_landmarks = landmarks
        self.__draw_filter = filter
        super().start()

    def stop(self):
        self.is_running = False
        self.terminate()
    
    def process_frame(self, frame):
        if self.is_running:
            self.__grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # VideoCapture uses BGR
            self.faces = self.__detector(self.__grayed_frame)
            self.draw_drawables(frame)

            # Emit signal with frame and detected faces
            self.frame_processed.emit(frame, self.faces)

    def get_landmarks(self, face):
        if self.__grayed_frame is not None:
            shape = self.__predictor(self.__grayed_frame, face)
            shape = self.convert_shape_to_numpy(shape)
            return shape

    def convert_shape_to_numpy(self, shape, dtype="int"):
        landmarks = np.zeros((68, 2), dtype=dtype)
        
        for i in range(0, 68):
            landmarks[i] = (shape.part(i).x, shape.part(i).y)
        
        return landmarks

    def midpoint (self, p1,p2):
        return int((p1.x +p2.x)/2), int((p1.y +p2.y)/2)
    
    def draw_drawables(self, frame):
        if len(self.faces) > 0:
            sticker = cv2.imread("package/resource/filter/cheek/pinkheart.png")
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            for face in self.faces:
                if self.__draw_rectangle:
                    x = face.left()
                    y = face.top()
                    w = face.right() - x
                    h = face.bottom() - y
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if self.__draw_landmarks:
                    for (x, y) in self.get_landmarks(face):
                        cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

                if self.__draw_filter:
                    try:
                        x, y = face.left() , face.top()
                        x1, y1 = face.right(), face.bottom()
                        landmarks = self.__predictor(gray, face)
                        left_pt = (landmarks.part(36).x, landmarks.part(36).y)
                        right_pt = (landmarks.part(39).x, landmarks.part(39).y)
                        sticker_width = int(hypot(left_pt[0]-right_pt[0], left_pt[1]-right_pt[1])*1.25)
                        sticker_height = int(sticker_width*.77)
                        
                        # Sticker Pos
                        p11 = (landmarks.part(1).x, landmarks.part(1).y)
                        p15 = (landmarks.part(15).x, landmarks.part(15).y)
                        p28 = (landmarks.part(28).x, landmarks.part(28).y)
                        p29 = (landmarks.part(29).x, landmarks.part(29).y)
                        pm1 = self.midpoint(landmarks.part(28), landmarks.part(29))
                        pm2 = ((p11[0] + pm1[0])/2, (p11[1] + pm1[1])/2)
                        pm3 = ((p15[0] + pm1[0])/2, (p15[1] + pm1[1])/2)
                        top_left1 = (int(pm2[0] - sticker_width/2), int(pm2[1] - sticker_height/2))
                        bot_right1 = (int(pm2[0] + sticker_width/2), int(pm2[1] + sticker_height/2))
                        top_left2 = (int(pm3[0] - sticker_width / 2), int(pm3[1] - sticker_height / 2))
                        bot_right2 = (int(pm3[0] + sticker_width / 2), int(pm3[1] + sticker_height / 2))
                        
                        # Adding sticker
                        sticker_img = cv2.resize(sticker, (sticker_width, sticker_height))
                        sticker_img_gray = cv2.cvtColor(sticker_img, cv2.COLOR_BGR2GRAY)
                        _, sticker_mask = cv2.threshold(sticker_img_gray, 25, 255, cv2.THRESH_BINARY_INV)
                        sticker_area1 = frame[top_left1[1]: top_left1[1] + sticker_height,
                                        top_left1[0]: top_left1[0] + sticker_width]
                        sticker_area2 = frame[top_left2[1]: top_left2[1] + sticker_height,
                                        top_left2[0]: top_left2[0] + sticker_width]
                        sticker_area_no_sticker1 = cv2.bitwise_and(sticker_area1, sticker_area1, mask=sticker_mask)
                        sticker_area_no_sticker2 = cv2.bitwise_and(sticker_area2, sticker_area2, mask=sticker_mask)
                        final_sticker1 = cv2.add(sticker_area_no_sticker1, sticker_img)
                        final_sticker2 = cv2.add(sticker_area_no_sticker2, sticker_img)
                        frame[top_left1[1]: top_left1[1] + sticker_height,
                            top_left1[0]: top_left1[0] + sticker_width] = final_sticker1
                        frame[top_left2[1]: top_left2[1] + sticker_height,
                            top_left2[0]: top_left2[0] + sticker_width] = final_sticker2
                    except:
                        pass
