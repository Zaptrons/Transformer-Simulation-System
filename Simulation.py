
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor


class Simulation:
    
    
    def __init__(self,transformer,daily_report,temp_sensor,load_sensor):
        self.transformer = transformer
        self.daily_report = daily_report
        self.temp_sensor = temp_sensor
        self.load_sensor = load_sensor
        
    def __get_hour_temp(self,season,hour):
        return self.temp_sensor.read_temperature(season,hour)
    def __get_hour_load(self,season,hour):
        return self.load_sensor.read_load(season,hour)

    def simulate_hour(self,season,hour):
        hour_ambient_temp = self.__get_hour_temp(season,hour)
        hour_load_profile = self.__get_hour_load(season,hour)
        self.transformer.update_status(hour_load_profile,hour_ambient_temp)
        status = {
            "Hour": hour,
            "Season": season,
             **self.transformer.get_status()
            }
        return status
    
    def simulate_day(self,season):
        for hour in range(24):
            self.daily_report.add_record(self.simulate_hour(season,hour))
 
