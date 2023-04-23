from package.vendor.gaze_tracking import GazeTracking


class GazeDetectionModule():
    def __init__(self):
        self.gaze_module = GazeTracking()

    def process_frame(self, grayed_frame, face):
        self.gaze_module.refresh(grayed_frame, face)
        return self.gaze_module.is_center()
