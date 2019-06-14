from .timing import minutes
from .delivery_operator import DeliveryOperator
from model.vehicles import Vehicle

class TransitVehicle(DeliveryOperator):
    def __init__(self, id, route, location="WHS"):
        super().__init__(id,route,location)
        self._model = Vehicle(speed=3.0)

