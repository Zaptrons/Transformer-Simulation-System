class LoadSensor:
    def read(self,season,hour):
        Load = self.environment.get_load_profile[season][hour]
        return Load 