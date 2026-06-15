from Enviroment import Environment
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor
from Simulation import Simulation
from Transformer import Transformer
from DailyReport import DailyReport

transformer = Transformer(input("Serial Nomber: "), int(input("Rated Power: ")))
environment= Environment()
daily_report = DailyReport()
simulation = Simulation(transformer,environment,daily_report)
print("========================") 
simulation.simulate("summer") 

max_ = daily_report.calculate_average_load()

print(max_) 
print("========================")  
print("========================") 
print("========================") 
        


