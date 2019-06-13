from .timing import minutes
from model.vehicles import Vehicle

class TransitVehicle:

    def __init__(self, id, route, location="WHS"):
        self.id = id
        self._location = location
        self._route = route
        self._storage = {}
        self._model = Vehicle(speed=2.0)

    def load(self, pallets):
        for p in pallets:
            self._storage[p.id] = p
        return True

    def drop(self, pallets_ids):
        dropped = []
        for pallet_id in pallets_ids:
            sup = self._storage.pop(pallet_id, None)
            if sup:
                dropped.append(sup)
        return dropped

    def drive_to(self, env, logger, stop, travel_time):
        logger.log(env.now, self.id, "going to %s" % stop)
        yield env.timeout(travel_time)
        self._location = stop
        logger.log(env.now, self.id, "arrived at %s" % stop)
    
    def process(self, env, logger, city):
        'the simpy process to simulate'
        for order in self._route:
            travel_time = city.travel_time(self._location,order["stop"],self._model) 
            yield env.process(self.drive_to(env,logger, order["stop"], travel_time))

