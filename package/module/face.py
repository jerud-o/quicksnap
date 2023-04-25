import os
import cv2
import dlib
from math import hypot

class FaceDetectionModule():
    def __init__(self):
        
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(os.path.join(os.getcwd(), "package/resource/shape_predictor_68_face_landmarks.dat"))
        self.__draw_filter_process = self.__draw_nothing

    def set_filter_path(self, filter_path=None, sticker_path=None):
        self.sticker = cv2.imread(os.path.join(os.getcwd(), sticker_path)) if sticker_path is not None else None

    def set_filter_method(self, filter_method="null"):
        match filter_method:
            case "cheek":
                self.__draw_filter_process = self.__draw_cheeks_sticker
            case "null":
                self.__draw_filter_process = self.__draw_nothing

    def process_frame(self, grayed_frame, frame_to_show, frame_to_print):
        self.__frame = grayed_frame
        self.faces = self.detector(self.__frame)

        if len(self.faces) > 0:
            for face in self.faces:
                self.__draw_filter_process(face, frame_to_show, frame_to_print)

    def __draw_cheeks_sticker(self, face, frame_to_show, frame_to_print):
        try:
            x, y = face.left() , face.top()
            x1, y1 = face.right(), face.bottom()
            landmarks = self.predictor(self.__frame, face)
            left_pt = (landmarks.part(36).x, landmarks.part(36).y)
            right_pt = (landmarks.part(39).x, landmarks.part(39).y)
            sticker_width = int(hypot(left_pt[0]-right_pt[0], left_pt[1]-right_pt[1])*1.25)
            sticker_height = int(sticker_width*.77)
            
            # Sticker Pos
            p11 = (landmarks.part(1).x, landmarks.part(1).y)
            p15 = (landmarks.part(15).x, landmarks.part(15).y)
            p28 = (landmarks.part(28).x, landmarks.part(28).y)
            p29 = (landmarks.part(29).x, landmarks.part(29).y)
            pm1 = self.__midpoint(landmarks.part(28), landmarks.part(29))
            pm2 = ((p11[0] + pm1[0])/2, (p11[1] + pm1[1])/2)
            pm3 = ((p15[0] + pm1[0])/2, (p15[1] + pm1[1])/2)
            top_left1 = (int(pm2[0] - sticker_width/2), int(pm2[1] - sticker_height/2))
            bot_right1 = (int(pm2[0] + sticker_width/2), int(pm2[1] + sticker_height/2))
            top_left2 = (int(pm3[0] - sticker_width / 2), int(pm3[1] - sticker_height / 2))
            bot_right2 = (int(pm3[0] + sticker_width / 2), int(pm3[1] + sticker_height / 2))
            
            # Adding sticker
            sticker_img = cv2.resize(self.sticker, (sticker_width, sticker_height))
            sticker_img_gray = cv2.cvtColor(sticker_img, cv2.COLOR_BGR2GRAY)
            _, sticker_mask = cv2.threshold(sticker_img_gray, 25, 255, cv2.THRESH_BINARY_INV)
            sticker_area1 = frame_to_print[top_left1[1]: top_left1[1] + sticker_height,
                            top_left1[0]: top_left1[0] + sticker_width]
            sticker_area2 = frame_to_print[top_left2[1]: top_left2[1] + sticker_height,
                            top_left2[0]: top_left2[0] + sticker_width]
            sticker_area_no_sticker1 = cv2.bitwise_and(sticker_area1, sticker_area1, mask=sticker_mask)
            sticker_area_no_sticker2 = cv2.bitwise_and(sticker_area2, sticker_area2, mask=sticker_mask)
            final_sticker1 = cv2.add(sticker_area_no_sticker1, sticker_img)
            final_sticker2 = cv2.add(sticker_area_no_sticker2, sticker_img)
            
            frame_to_show[top_left1[1]: top_left1[1] + sticker_height, top_left1[0]: top_left1[0] + sticker_width] = final_sticker1
            frame_to_show[top_left2[1]: top_left2[1] + sticker_height, top_left2[0]: top_left2[0] + sticker_width] = final_sticker2
            frame_to_print[top_left1[1]: top_left1[1] + sticker_height, top_left1[0]: top_left1[0] + sticker_width] = final_sticker1
            frame_to_print[top_left2[1]: top_left2[1] + sticker_height, top_left2[0]: top_left2[0] + sticker_width] = final_sticker2
        except:
            pass
    
    def __midpoint(self, p1,p2):
        return int((p1.x +p2.x)/2), int((p1.y +p2.y)/2)
    
    def __draw_nothing(*_):
        pass