from Clock import Clock

class TimeEngine:

    def __init__(self, clock, calendar):
        self.clock = clock
        self.calendar = calendar

    def get_hours_in_day(self):
        return self.clock.HOURS_IN_DAY
    
    def get_days_in_month(self):
        return self.calendar.get_days_in_month()
    
    def get_month_in_year(self):
        return self.calendar.get_month_in_year()
        
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

        if self.clock.is_new_day():
            self.calendar.next_day()
    
    
