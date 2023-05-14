from package.vendor.gaze_tracking import GazeTracking


class GazeDetectionModule():
    def __init__(self):
        self.gaze_module = GazeTracking()

    def process_frame(self, grayed_frame, face):
        try:
            self.gaze_module.refresh(grayed_frame, face)
            # return self.gaze_module.is_center()
            is_x_centered = 0.4 < self.gaze_module.horizontal_ratio() < 0.6
            is_y_centered = 0.6 < self.gaze_module.vertical_ratio() < 0.85
            # print(self.gaze_module.vertical_ratio())
            # print(is_x_centered, is_y_centered)
            return is_x_centered and is_y_centered
        except:
            return False
