from PyQt6.QtCore import pyqtSignal, QTimer

class CountdownTimerModule():
    countdown_timer_updated = pyqtSignal(str)
    countdown_timer_finished = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__COUNTDOWN_TIMER_DURATION = 3
        self.__countdown_time_left = self.__COUNTDOWN_TIMER_DURATION
        self.__countdown_timer = QTimer(timeout=self._update_countdown_timer)

    def _start_countdown_timer(self):
        if not self.__countdown_timer.isActive():
            self.__countdown_timer.start(1000)
            self.countdown_timer_updated.emit(str(self.__countdown_time_left))

    def _stop_countdown_timer(self):
        self.__countdown_timer.stop()
        self.countdown_timer_updated.emit("")
        self.__countdown_time_left = self.__TIMER_DURATION

    def _update_countdown_timer(self):
        self.__countdown_time_left -= 1

        if self.__countdown_time_left == 0:
            self.__stop_countdown_timer()
            self.countdown_timer_finished.emit()
            return

        self.countdown_timer_updated.emit(str(self.__countdown_time_left))

        