
class TemperatureSensor:
    def __init__(self,environment):
        self.environment = environment

    def read_temperature(self,season,hour):
         return self.environment.get_hour_temperature(season,hour)
      