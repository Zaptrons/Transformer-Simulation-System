from Enviroment import Environment
from Sensors.Load_Sensor import LoadSensor
from Sensors.Temperature_sensor import TemperatureSensor
from Simulation import Simulation
from Transformer import Transformer

TR = Transformer(input("Serial Nomber: "), int(input("Rated Power: ")))
env = Environment()


Sim = Simulation(TR,env)
print("========================") 
Sim.simulate("summer") 
max_temp = Sim.find_max_temperature()
Sim.print(max_temp.items())
print("========================")
min_temp = Sim.find_min_temperature()
Sim.print(min_temp.items())
print("========================") 
max_load = Sim.find_max_load()
Sim.print(max_load.items())
print("========================") 
min_load = Sim.find_min_load()
Sim.print(min_load.items())
print("========================")  
ave_temp = Sim.calculate_average_temperature()
print(f"{ave_temp:.3f}") 
print("========================")  
ave_load = Sim.calculate_average_load()
print(f"{ave_load:.3f}")
print("========================")  


        


