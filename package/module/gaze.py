from package.vendor.gaze_tracking import GazeTracking


class GazeDetectionModule():
    def __init__(self):
        self.gaze_module = GazeTracking()

    def process_frame(self, grayed_frame, face):
        try:
            self.gaze_module.refresh(grayed_frame, face)
            is_x_centered = 0.4 < self.gaze_module.horizontal_ratio() < 0.6
            is_y_centered = 0.75 < self.gaze_module.vertical_ratio() < 0.8
            print(is_x_centered, is_y_centered)
            return is_x_centered and is_y_centered
        except:
            return False
