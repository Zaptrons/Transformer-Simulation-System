class Clock:
    HOURS_IN_DAY = 24

    def __init__(self):
        self.hour = 0

    def tick(self):
        self.hour += 1

    def get_hour(self):
        return self.hour

    def reset(self):
        self.hour = 0