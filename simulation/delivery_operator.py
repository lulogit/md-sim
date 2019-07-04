from .timing import minutes

class DeliveryOperator:
    def __init__(self, id, route, location="WHS_001"):
        self.id = id
        self._location = location
        self._route = route
        self._storage = set()
        self._model = None #Vehicle(speed=2.0)

    def load(self, sim, units, store):
        'the simpy process of loading some units'
        sim.logger.log(sim.env.now, self.id, "loading %s from %s" % (str(units),store))
        if store in sim.micro_hubs:
            while units:
                sim.logger.log(sim.env.now, self.id, "waiting for %s from %s" % (str(units),store))
                taken_unit = yield sim.micro_hubs[store].take_sup(units)
                sim.logger.log(sim.env.now, self.id, "moving %s" % (taken_unit))
                self._storage.add(taken_unit)
                yield sim.env.timeout(minutes(2))
                sim.logger.log(sim.env.now, self.id, "moved %s" % (taken_unit))
                units.remove(taken_unit)
        else:
            self._storage |= set(units)
            yield sim.env.timeout(len(units)*minutes(2))
        sim.logger.log(sim.env.now, self.id, "finished loading %s" % str(units))
        return True

    def drop(self, sim, units, store):
        'the simpy process of dropping some units'
        sim.logger.log(sim.env.now, self.id, "delivering %s" % str(units))
        if store in sim.micro_hubs:
            for unit in units:
                sim.logger.log(sim.env.now, self.id, "waiting for space from %s" % (store))
                yield sim.micro_hubs[store].put_sup(unit)
                yield sim.env.timeout(minutes(3))
                self._storage.remove(unit)
                sim.logger.log(sim.env.now, self.id, "put %s into %s" % (unit,store))
        else:
            self._storage -= set(units)
            yield sim.env.timeout(len(units)*minutes(3))
        sim.logger.log(sim.env.now, self.id, "delivered %s" % str(units))
        return True
    
    def drive_to(self, sim, stop, travel_time):
        'the simpy process of driving to a location'
        sim.logger.log(sim.env.now, self.id, "going to %s" % stop)
        yield sim.env.timeout(travel_time)
        self._location = stop
        sim.logger.log(sim.env.now, self.id, "arrived at %s" % stop)
    
    def route_loop(self, sim):
        'the simpy process of following a route'
        for order in self._route:
            travel_time = sim.city.travel_time(self._location,order["stop"],self._model) 
            yield sim.env.process(self.drive_to(sim, order["stop"], travel_time))
            if order["drop"]:
                yield sim.env.process(self.drop(sim, order["drop"], order["stop"]))
            if order["take"]:
                yield sim.env.process(self.load(sim, order["take"], order["stop"]))
