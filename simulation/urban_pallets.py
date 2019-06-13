
class SUP:

    def __init__(self, parcels=[]):
        self._parcels = {p.id: p for p in parcels}

    def take(self, parcel_id):
        p = self._parcels.pop(parcel_id, None)
        return p

    def is_empty(self):
        return not self._parcels
