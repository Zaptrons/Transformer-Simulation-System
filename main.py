from Environment import Environment
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor
from Simulation import Simulation
from Transformer import Transformer
from DailyReport import DailyReport
from Clock import Clock
from Calendar import Calendar
from TimeEngine import TimeEngine

clock = Clock()
calendar = Calendar()
time_engine = TimeEngine(clock,calendar)
transformer = Transformer(input("Serial Nomber: "), int(input("Rated Power: ")))
environment= Environment()
daily_report = DailyReport()
temperature_sensor = TemperatureSensor(environment)
load_sensor = LoadSensor(environment)
simulation = Simulation(transformer,daily_report,temperature_sensor,load_sensor,time_engine)


print("========================") 

simulation.simulate_year()
daily_report.print_report()

