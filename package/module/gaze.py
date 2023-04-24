from package.vendor.gaze_tracking import GazeTracking


class GazeDetectionModule():
    def __init__(self):
        self.gaze_module = GazeTracking()
        self.UPPER_BOUNDS = 0.6
        self.LOWER_BOUNDS = 0.4

    def process_frame(self, grayed_frame, face):
        self.gaze_module.refresh(grayed_frame, face)
        is_x_centered = self.LOWER_BOUNDS < self.gaze_module.horizontal_ratio() < self.UPPER_BOUNDS
        is_y_centered = self.LOWER_BOUNDS < self.gaze_module.vertical_ratio() < self.UPPER_BOUNDS
        return is_x_centered and is_y_centered
