import simpy
from .logging import StrLog

class Simulation:

    def __init__(self, routes, topo, params):
        self._SUPs = routes["SUPs"]
        self._TVs = routes["TVs"]
        self._PVs = routes["PVs"]
        self._city = topo
        self._log = StrLog()

    def run(self, seed, time=None):
        '''
            Execute the simulation up to time <time>, returning the log of the simulation.
        '''
        
        return self._log.to_list()
