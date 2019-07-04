import simpy
from .logging import StrLog
from .city import City
from .micro_hubs import MicroHub
from .transit_vehicles import TransitVehicle
from .proximity_vehicles import ProximityVehicle
from . import random_noise as noise

class Simulation:

    def __init__(self, routes, topo, params):
        self.city = City(noise, topo["locations"])
        self.env = simpy.Environment()
        self.logger = StrLog()

        # init Transit vehicles
        self._transit_vehicles = [
            TransitVehicle(van_id,route)
            for van_id, route in routes["TVs"].items()]
        for tv in self._transit_vehicles:
            self.env.process(tv.route_loop(self))

        # init Proximity vehicles
        self._proximity_vehicles = [
            ProximityVehicle(biker_id,route)
            for biker_id, route in routes["PVs"].items()]
        for pv in self._proximity_vehicles:
            self.env.process(pv.route_loop(self))
        
        # init micro hubs
        self.micro_hubs = {mh_id: MicroHub(self, mh_id) for mh_id in ["MH_001"]}

    def run(self, seed, time=None):
        '''
            Execute the simulation up to time <time>, returning the log of the simulation.
        '''
        noise.set_seed(seed)
        self.env.run()
        return self.logger.to_list()
