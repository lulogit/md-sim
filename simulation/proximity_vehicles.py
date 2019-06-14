from .timing import minutes
from .delivery_operator import DeliveryOperator
from model.vehicles import Vehicle

class ProximityVehicle(DeliveryOperator):
    def __init__(self, id, route, location="SQUARE"):
        super().__init__(id,route,location)
        self._model = Vehicle(speed=1.0)

