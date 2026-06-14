
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor

# 
class Simulation:
    
    
    def __init__(self,transformer,environment):
        self.transformer = transformer
        self.environment = environment
        self.daily_report = []
        

    def simulate(self,season):
        for hour in range(24):
            hour_ambient_temp = self.environment.get_hour_temperature(season,hour)
            hour_load_profile = self.environment.get_hour_load_profile(season,hour)
            self.transformer.update_status(hour_load_profile,hour_ambient_temp)
            status = {
                "Hour": hour,
                 **self.transformer.get_status()
                }
            self.daily_report.append(status)
            
                  
    def print_report(self):
        for report in self.daily_report:
            for key , value in report.items():
                print(f"{key} : {value}")
            print("------------------------")  


    def find_max_temperature(self):
        if not self.daily_report:
            return None
        max_temp_dic = self.daily_report[0]
        for report in self.daily_report:
            if report["Temperature"] > max_temp_dic["Temperature"]:
                max_temp_dic = report
        return max_temp_dic           
        
    def find_min_temperature(self):
        if not self.daily_report:
            return None
        min_temp_dic = self.daily_report[0]
        for report in self.daily_report:
            if report["Temperature"] < min_temp_dic["Temperature"]:
                min_temp_dic = report
        return min_temp_dic
    
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
    
    def print(self,dic_to_print):
        for key,value in dic_to_print:
            print(f"{key} :{value}")



    
