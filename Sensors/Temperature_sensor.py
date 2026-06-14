
class TemperatureSensor:
    def read(self,season,hour):
        Temp = self.environment.get_temperature[season][hour]
        return Temp