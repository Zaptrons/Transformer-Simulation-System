
class Environment:
    temperatures = {
            "summer": {
                0: 25, 1: 25, 2: 24, 3: 24, 4: 23, 5: 23,
                6: 22, 7: 22, 8: 22, 9: 23, 10: 23, 11: 24,
                12: 25, 13: 27, 14: 29, 15: 31, 16: 32,
                17: 31, 18: 29, 19: 27, 20: 25,
                21: 24, 22: 24, 23: 24
            }
        }
        
    load_profile = {
            "summer": {
                0: 35, 1: 30, 2: 30, 3: 28, 4: 28, 5: 30,
                6: 40, 7: 50, 8: 60, 9: 75,
                10: 85, 11: 95, 12: 100, 13: 100, 14: 95, 15: 90,
                16: 80, 17: 75, 18: 80,
                19: 95, 20: 100, 21: 95, 22: 85,
                23: 60
            }
        }

    def get_hour_temperature(self,season, hour):
        return self.temperatures[season][hour]
    
    def get_hour_load_profile(self,season, hour):
        return self.load_profile[season][hour]
