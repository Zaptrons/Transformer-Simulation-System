class Clock:
    HOURS_IN_DAY = 24

    def __init__(self):
        self.hour = 0
        self._new_day = False

    def tick(self):
        self.hour += 1

        if self.hour >= self.HOURS_IN_DAY:
            self.__reset()
            return
        
        self._new_day = False

    def get_hour(self):
        return self.hour

    def __reset(self):
        self.hour = 0
        self._new_day = True

    def is_new_day(self):
        return self._new_day