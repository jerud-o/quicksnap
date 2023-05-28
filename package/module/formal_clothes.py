import cv2
from main import resource_path

class FormalClothesModule():
    def __init__(self):
        self.__male = cv2.imread(resource_path("package\\resource\\formal\\male.png"), cv2.IMREAD_UNCHANGED)
        self.__female = cv2.imread(resource_path("package\\resource\\formal\\female.png"), cv2.IMREAD_UNCHANGED)

    def set_gender(self, gender):
        self.__gender = gender

        if self.__gender == 1:
            self.__image = self.__male
        elif self.__gender == 2:
            self.__image = self.__female

    def process_frame(self, frame_to_show, frame_to_print):
        h, w, _ = frame_to_show.shape

        height_ratio = h / self.__image.shape[0]
        new_image_height = int(self.__image.shape[0] * height_ratio)
        self.__image = cv2.resize(self.__image, (w, new_image_height))
        
        x_pos = 0
        y_pos = new_image_height - h
        
        alpha_s = self.__image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        
        for c in range(0, 3):
            frame_to_show[y_pos:y_pos+new_image_height, x_pos:x_pos+self.__image.shape[1], c] = (alpha_s * self.__image[:, :, c] + alpha_l * frame_to_show[y_pos:y_pos+new_image_height, x_pos:x_pos+self.__image.shape[1], c]).astype(int)
            frame_to_print[y_pos:y_pos+new_image_height, x_pos:x_pos+self.__image.shape[1], c] = (alpha_s * self.__image[:, :, c] + alpha_l * frame_to_print[y_pos:y_pos+new_image_height, x_pos:x_pos+self.__image.shape[1], c]).astype(int)
