import os
import cv2

class FormalClothesModule():
    def __init__(self):
        self.__male = cv2.imread(os.path.join(os.getcwd(), "package/resource/formal/male.png"), cv2.IMREAD_UNCHANGED)
        self.__male_dim = self.__male.shape
        self.__female = cv2.imread(os.path.join(os.getcwd(), "package/resource/formal/female.png"), cv2.IMREAD_UNCHANGED)
        self.__female_dim = self.__female.shape

    def set_gender(self, gender):
        self.__gender = gender

        if self.__gender == 1:
            self.__image = self.__male
            self.__image_dim = self.__male_dim
        elif self.__gender == 2:
            self.__image = self.__female
            self.__image_dim = self.__female_dim

    def process_frame(self, frame_to_show, frame_to_print):
        h, w, _ = frame_to_show.shape
        w = int((w - h) / 2)

        x_pos = int((frame_to_show.shape[1] - self.__image_dim[1]) / 2)
        y_pos = int((frame_to_show.shape[0] - self.__image_dim[0]) / 2)

        alpha_s = self.__image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        
        for c in range(0, 3):
            frame_to_show[y_pos:y_pos+self.__image_dim[0], x_pos:x_pos+self.__image_dim[1], c] = (alpha_s * self.__image[:, :, c] + alpha_l * frame_to_show[y_pos:y_pos+self.__image_dim[0], x_pos:x_pos+self.__image_dim[1], c]).astype(int)
            frame_to_print[y_pos:y_pos+self.__image_dim[0], x_pos:x_pos+self.__image_dim[1], c] = (alpha_s * self.__image[:, :, c] + alpha_l * frame_to_print[y_pos:y_pos+self.__image_dim[0], x_pos:x_pos+self.__image_dim[1], c]).astype(int)
