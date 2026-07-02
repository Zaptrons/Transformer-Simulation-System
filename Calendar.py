# Calendar.py
class Calendar:

    DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTHS_IN_YEAR = 12

    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 0
        self._new_month = False
        self._new_year = False

    def next_day(self):
        self.__update_day()
          
    def __update_day(self):
        days = self.get_days_in_month()
        if self.day < days:
            self.day += 1
            return
        
        self.day = 1
        self._new_month = True
        self.__update_month()

    def __update_month(self):
        if self.month < 12: 
            self.month += 1
            return
        
        self.month = 1
        self._new_year = True
        self.__update_year()

    def __update_year(self):
        self.year += 1

#------------------------------
# getters
#------------------------------
       
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    
    def get_season(self):
        if self.month in (12, 1, 2):
            return "Winter"
        elif self.month in (3, 4, 5):
            return "Spring"
        elif self.month in (6, 7, 8):
            return "Summer"
        else:
            return "Autumn"
        
    def get_days_in_month(self):
        return self.DAYS_IN_MONTH[self.month - 1]
    
    def get_month_in_year(self):
        return self.MONTHS_IN_YEAR
    
#------------------------------
# query
# -----------------------------


    def is_new_month(self):
        result = self._new_month
        self._new_month = False
        return result

    def is_new_year(self):
        result = self._new_year
        self._new_year = False
        return result




    