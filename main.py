from Environment import Environment
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor
from Simulation import Simulation
from Transformer import Transformer
from DailyReport import DailyReport

transformer = Transformer(input("Serial Nomber: "), int(input("Rated Power: ")))
environment= Environment()
daily_report = DailyReport()
temperature_sensor = TemperatureSensor(environment)
load_sensor = LoadSensor(environment)
simulation = Simulation(transformer,daily_report,temperature_sensor,load_sensor)
print("========================") 
status = simulation.simulate_hour("summer", 14)
for key,value in status.items():
    print(f"{key} : {value}")

