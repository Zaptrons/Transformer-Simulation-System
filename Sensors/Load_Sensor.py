class LoadSensor:
    def __init__(self,environment):
        self.environment = environment

    def read_load(self,season,hour):
        return self.environment.get_hour_load_profile(season,hour)
         