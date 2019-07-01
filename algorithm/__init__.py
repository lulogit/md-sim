import random

def plan_delivery(orders,fleet,topology) -> "plan":
    '''
        inputs:
            * list of parcels to deliver (with destination address, weight, and dimensions)
            * list of vehicles and micro hubs in the fleet, available number of sups
            * locations of point of interests in the city
        outputs:
            * list of parcels per SUP
            * route, as list of (stop, SUPs to drop, SUPs to take) for each vehicle
    '''
    # simplest algorithm: no brainer
    plan = {}
    # 1. assign parcels to random SUPs
    parcels_per_sup = fleet["sups"]["max_parcels"]
    def sup_id(i):
        return "%s%03d" % (fleet["sups"]["id_prefix"], i)
    plan["SUPs"] = {sup_id(i):}
    # 2. assign SUPs to Transit Vehicles
    # 3. route for each transit vehicle
    # 4. assign SUPs to Proximity Vehicles
    # 5. Proximity Vehicles' routing
    return plan 
