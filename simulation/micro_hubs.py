from model import micro_hubs
import simpy

class MicroHub:

    def __init__(self, sim, id):
        self.id = id
        model = micro_hubs.MicroHub()
        self._unfolded_storage = simpy.FilterStore(sim.env,capacity=model.unfolded_capacity)
        self._folded_storage = simpy.Store(sim.env, capacity=model.folded_capacity)

    def put_sup(self, sup):
        'add a Smart Urban Pallet to the MH'
        return self._unfolded_storage.put(sup)

    def take_sup(self, sup):
        return self._unfolded_storage.get(lambda unit: unit==sup)

    def return_folded_sup(self,sup):
        yield self._folded_storage.put(sup)

    def collect_folded_sup(self,sup):
        unit = yield self._folded_storage.get(lambda unit: unit == sup)
        return unit
