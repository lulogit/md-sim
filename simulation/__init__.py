import simpy
from .logging import StrLog
from .city import City
from .transit_vehicles import TransitVehicle
from . import random_noise as noise

class Simulation:

    def __init__(self, routes, topo, params):
        self._city = City(noise, topo["locations"])
        self._env = simpy.Environment()
        self._log = StrLog()

        # init Transit vehicles
        self._transit_vehicles = [
            TransitVehicle(van_id,route)
            for van_id, route in routes["TVs"].items()]
        for tv in self._transit_vehicles:
            self._env.process(tv.process(self._env, self._log, self._city))

    def run(self, seed, time=None):
        '''
            Execute the simulation up to time <time>, returning the log of the simulation.
        '''
        noise.set_seed(seed)
        self._env.run()
        return self._log.to_list()
