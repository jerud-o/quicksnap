import winsound
import time
from PyQt6.QtCore import QObject, pyqtSignal, QTimer


class CountdownTimerModule(QObject):
    ticked = pyqtSignal(int)
    finished = pyqtSignal()
    
    def __init__(self, duration=3):
        super().__init__()
        self.TIMER_DURATION = duration
        self.time_left = self.TIMER_DURATION
        self.timer = QTimer(timeout=self.__tick)

        self.FREQUENCY = 1000 # Hz
        self.BEEP_DURATION = 250 # msecs

    def start(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            winsound.Beep(self.FREQUENCY, self.BEEP_DURATION)
            self.ticked.emit(self.time_left)

    def stop(self, forced=False):
        self.timer.stop()
        self.killTimer(self.timer.timerId())
        
        if not forced:
            self.finished.emit()
            self.__shutter_sound()
        
        self.ticked.emit(0)
        # Reset timer
        self.time_left = self.TIMER_DURATION
        return

    def __tick(self):
        self.time_left -= 1
        
        if self.time_left == 0:
            self.stop()
            return
        
        winsound.Beep(self.FREQUENCY, self.BEEP_DURATION)
        self.ticked.emit(self.time_left)

    def __shutter_sound(self):
        for i in range(2):
            winsound.Beep(1500, 100)
            time.sleep(20 / 1000)
