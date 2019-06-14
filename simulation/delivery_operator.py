from .timing import minutes

class DeliveryOperator:
    def __init__(self, id, route, location="WHS"):
        self.id = id
        self._location = location
        self._route = route
        self._storage = set()
        self._model = None #Vehicle(speed=2.0)

    def load(self, env, logger, units):
        'the simpy process of loading some units'
        logger.log(env.now, self.id, "loading %s" % str(units))
        self._storage |= set(units)
        yield env.timeout(len(units)*minutes(2))
        logger.log(env.now, self.id, "finished loading %s" % str(units))
        return True

    def drop(self, env, logger, units):
        'the simpy process of dropping some units'
        self._storage -= set(units)
        logger.log(env.now, self.id, "delivering %s" % str(units))
        yield env.timeout(len(units)*minutes(3))
        logger.log(env.now, self.id, "delivered %s" % str(units))
        return True
    
    def drive_to(self, env, logger, stop, travel_time):
        'the simpy process of driving to a location'
        logger.log(env.now, self.id, "going to %s" % stop)
        yield env.timeout(travel_time)
        self._location = stop
        logger.log(env.now, self.id, "arrived at %s" % stop)
    
    def route_loop(self, env, logger, city):
        'the simpy process of following a route'
        for order in self._route:
            travel_time = city.travel_time(self._location,order["stop"],self._model) 
            yield env.process(self.drive_to(env,logger, order["stop"], travel_time))
            if order["drop"]:
                yield env.process(self.drop(env,logger, order["drop"]))
            if order["take"]:
                yield env.process(self.load(env,logger, order["take"]))
