
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor

# 
class Simulation:
    
    
    def __init__(self,transformer,environment,daily_report):
        self.transformer = transformer
        self.environment = environment
        self.daily_report = daily_report
        

    def simulate(self,season):
        for hour in range(24):
            hour_ambient_temp = self.environment.get_hour_temperature(season,hour)
            hour_load_profile = self.environment.get_hour_load_profile(season,hour)
            self.transformer.update_status(hour_load_profile,hour_ambient_temp)
            status = {
                "Hour": hour,
                 **self.transformer.get_status()
                }
            self.daily_report.add_record(status)
 
