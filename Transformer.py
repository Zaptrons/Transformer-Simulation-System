class Transformer:
    def __init__(self,serial_number,rated_power):
        self.serial_number = serial_number
        self.rated_power = rated_power
        self.temperature = 20
        self.current_load = 0
        self.load_percentage = 0
        
        
    def __calculate_temperature(self, hour_ambient_temp):
        self.temperature = hour_ambient_temp + (self.load_percentage * 0.5)
        

    def __calculate_current_load(self,hour_load_profile):
        self.hour_load_profile = hour_load_profile
        self.current_load = self.rated_power * (hour_load_profile / 100)
        

    def update_status(self, hour_load_profile, hour_ambient_temp):
        self.load_percentage = hour_load_profile
        self.__calculate_current_load(hour_load_profile)
        self.__calculate_temperature(hour_ambient_temp)

    def get_status(self):
        return {
            "Serial Number": self.serial_number,
            "Rated Power": self.rated_power,
            "Temperature": self.temperature,
            "Current Load": self.current_load,
            "Load Percentage": self.load_percentage
        }