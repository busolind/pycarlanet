import abc

import carla

from utils.decorators import preconditions


# Decorator for carla.Actor
# NOTE: you can call each method of carla.Actor on this class, but if you want to pass an object of type
# CarlaInetActor to a methods defined in carla you have to pass the attribute carla_actor
# because carla can't see this class
class CarlaInetActor(abc.ABC):

    def __init__(self, carla_actor: carla.Actor):
        self._carla_actor = carla_actor

    @preconditions('_carla_actor')
    def __getattr__(self, *args):
        return self._model.__getattribute__(*args)

    def init_actor(self, configuration):
        ...

    def alive(self):
        ...
