import carla
import random

#init the carla environment
# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

try:
    print(client.replay_file("/home/egu/CARLA_0.9.13/PythonAPI/examples/test_recording.log", 1, 100, 1))
    
except:
    pass
