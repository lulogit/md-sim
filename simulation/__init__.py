
class Simulation:

    def __init__(self, routes, params):
        self._SUPs = routes["SUPs"]
        self._TVs = routes["TVs"]
        self._PVs = routes["PVs"]

    def run(self, time=None):
        '''
            Execute the simulation up to time <time>, returning the log of the simulation.
        '''
        return []
