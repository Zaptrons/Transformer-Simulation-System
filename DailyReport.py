class DailyReport:
    def __init__(self):
        self.daily_report = []

    def add_record(self,report):
        self.daily_report.append(report)

    def print_report(self):
        for report in self.daily_report:
            for key,value in report.items():
                print(f"{key} : {value}")
            print("------------------------")

    def find_max_temperature(self):
        if not self.daily_report:
            return None
        max_temp = self.daily_report[0]
        for report in self.daily_report:
            if report["Temperature"] > max_temp["Temperature"]:
                max_temp = report
        return max_temp  

    def find_min_temperature(self):
        if not self.daily_report:
            return None
        min_temp = self.daily_report[0]
        for report in self.daily_report:
            if report["Temperature"] < min_temp["Temperature"]:
                min_temp = report
        return min_temp

    def find_max_load(self):
        if not self.daily_report:
            return None
        max_load = self.daily_report[0]
        for report in self.daily_report:
            if report["Load Percentage"] > max_load["Load Percentage"]:
                max_load = report
        return max_load

    def find_min_load(self):
        if not self.daily_report:
            return None
        min_load = self.daily_report[0]
        for report in self.daily_report:
            if report["Load Percentage"] < min_load["Load Percentage"]:
                min_load = report
        return min_load

    def calculate_average_temperature(self):
        if not self.daily_report:
            return None
        average_temp = (sum(report["Temperature"] for report in self.daily_report)/len(self.daily_report))
        return average_temp
    
    def calculate_average_load(self):
        if not self.daily_report:
            return None
        average_load = (sum(report["Load Percentage"] for report in self.daily_report)/len(self.daily_report))
        return average_load