#建立carla和python的桥梁
import glob
import os
import sys
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random

#init the carla environment
# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

#spawn a actor and get its information
transform = carla.Transform()
transform = random.choice(world.get_map().get_spawn_points())
print(transform)
actor = world.spawn_actor(random.choice(world.get_blueprint_library().filter('*vehicle*')), transform)
actor.set_transform(transform)
print(actor.get_transform())
# print(actor.get_velocity())

#观察视角追踪某个actor
spectator = world.get_spectator()
transform = actor.get_transform()
spectator.set_transform(carla.Transform(transform.location + carla.Location(z=20),
                                                    carla.Rotation(pitch=-90)))
print(actor.get_transform())
print(spectator.get_transform())
#为什么这两个值的xy不对应？？？？？？


# destroyed_sucessfully = actor.destroy() # Returns True if successful


#actor_list = world.get_actors()#储存Vehicle集合的数据结构

# Find an actor by id.
# actor = actor_list.find(1)
# Print the location of all the speed limit signs in the world.
# for vehicle in actor_list.filter('vehicle*'):
#     print(vehicle.get_location())
#     vehicle.destroy()
    
    