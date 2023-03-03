import carla
import random

#init the carla environment
# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()


#load world
#print(client.get_available_maps())#print loadable maps in carla
world = client.load_world('Town01')#load a new map


#spectator
# Retrieve the spectator object
spectator = world.get_spectator()
# Get the location and rotation of the spectator through its transform
transform = spectator.get_transform()
print(transform)
location = transform.location
rotation = transform.rotation

# Set the spectator with an empty transform
spectator.set_transform(carla.Transform())
spectator.set_transform(transform)
# This will set the spectator at the origin of the map, with 0 degrees
# pitch, yaw and roll - a good way to orient yourself in the map


#adding NPCs
#spawn NPC vehicles
vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')# vehicle_blueprints is a pool of vehicles to chooce. Get the blueprint library and filter for the vehicle blueprints
spawn_points = world.get_map().get_spawn_points()# Get a set of the map's spawn points
for i in range(0,50):# Spawn 50 vehicles randomly distributed throughout the map 
    world.try_spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))
#spawn ego vehicle
ego_vehicle = world.spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))#carla.Client.world.spawn_actor(<object type>, <spawn location>, <attach_to>) if attach_to=x exists, <spawn location> is relative to x 
transform = ego_vehicle.get_transform()



#add sensors
#set camera
camera_init_trans = carla.Transform(carla.Location(z=1.5))# Create a transform to place the camera on top of the vehicle  
camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')# We create the camera through a blueprint that defines its properties
camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to=ego_vehicle)# We spawn the camera and attach it to our ego vehicle
#get sensor data: Start camera with PyGame callback
camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))

#activate NPCs
for vehicle in world.get_actors().filter('*vehicle*'):
    vehicle.set_autopilot(True)
    
try:
    client = carla.Client('localhost', 2000)
    world = client.get_world()

    print(client.start_recorder("/home/egu/CARLA_0.9.13/PythonAPI/examples/wmy/recording01.log", True))#这个log文件不是给人看的，而是用来复现仿真的   

finally:    
    client.stop_recorder()
    
