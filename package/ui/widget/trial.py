class FaceDetectionThread(QThread):
    frame_processed = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super(FaceDetectionThread, self).__init__(parent)
        
        # Dlib's Configuration
        self.__detector = dlib.get_frontal_face_detector()
        self.__predictor = dlib.shape_predictor("package/resource/shape_predictor_68_face_landmarks.dat")
        self.mustache = cv2.imread("package/resource/filter/mustache.png", -1)

    def start(self, rectangle=False, landmarks=False, filter=False):
        self.is_running = True
        self.__draw_rectangle = rectangle
        self.__draw_landmarks = landmarks
        self.__draw_filter = filter
        super().start()

    def stop(self):
        self.terminate()

    def set_variables(self, frame_drawn, grayed_frame):
        self.__frame_drawn = frame_drawn
        self.__grayed_frame = grayed_frame
        
    def process_frame(self):
        self.faces = self.__detector(self.__grayed_frame)
        self.draw_drawables()
            
    def get_landmarks(self, face):
        shape = self.__predictor(self.__grayed_frame, face)
        shape = self.convert_shape_to_numpy(shape)
        return shape
            
    def convert_shape_to_numpy(self, shape, dtype="int"):
        landmarks = np.zeros((68, 2), dtype=dtype)
        
        for i in range(0, 68):
            landmarks[i] = (shape.part(i).x, shape.part(i).y)
        
        return landmarks

    def midpoint(self, p1, p2):
        return int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)
    
    def draw_drawables(self):
        if len(self.faces) > 0:
            gray = self.__grayed_frame

            for face in self.faces:
                if self.__draw_rectangle:
                    x = face.left()
                    y = face.top()
                    w = face.right() - x
                    h = face.bottom() - y
                    cv2.rectangle(self.__frame_drawn, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if self.__draw_landmarks:
                    for (x, y) in self.get_landmarks(face):
                        cv2.circle(self.__frame_drawn, (x, y), 2, (0, 0, 255), -1)

                if self.__draw_filter:
                    nose_tip = self.get_landmarks(face)[33]
                    left_mouth = self.get_landmarks(face)[51]
                    right_mouth = self.get_landmarks(face)[57]
                    midpoint_mouth = self.midpoint(left_mouth, right_m
