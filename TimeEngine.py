from Clock import Clock

class TimeEngine:

    def __init__(self, clock, calendar):
        self.clock = clock
        self.calendar = calendar

    def get_time(self):
        return {
            "Hour": self.clock.get_hour(),
            "Day": self.calendar.get_day(),
            "Month": self.calendar.get_month(),
            "Year": self.calendar.get_year(),
            "Season": self.calendar.get_season()
        }

    def next_time(self):

        self.clock.tick()

        if self.clock.get_hour() >= Clock.HOURS_IN_DAY:
            self.clock.reset()
            self.calendar.next_day()