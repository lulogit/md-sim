# Blink, Multimodal Delivery Algorithm + Simulation Tool

### The problem
Parcels are delivered in the city using both vans and bikers, from a wharehouse. 

### The idea
* Micro Hubs (MH) are lockers displaced in the city, acting as buffer between vans and bikers.
* Parcels are grouped into Smart Urban Pallets (SUP), boxes that can be easily carried by bikers or stored into the Micro Hubs
* Wharehouses (WHS) package the parcels into Smart Urban Pallets.
* Vans/Transit Vehicles (TV) deliver SUPs into the Micro Hubs, through a route.
* Bikers/Proximity vehicles (PV) deliver SUPs from the micro hubs to the delivery points (DP), though a route.
* Bikers (PV) deliver the empty, foldable, SUPs back into the Micro Hubs.
* Vans (TV) deliver empty, folded, SUPs back to wharehouses.

### KPI
1. delivery speed: how fast the parcel is delivered
2. delivery precision: the parcel is correctly delivered in a requested time slot
3. delivery time coverage: parcels are delivered in unusual time slots (e.g: night)
3. customer communication: customer is notified of change of plans, delivery time, ...

### Usage
#### Installation
Use ```pip install -r requirements.txt``` to install all the dependencies.
#### Execution
To run the simulation, use the ```simulate``` command line tool.

### V0.1
#### Assumptions
1. Next day delivery / no time slot / no pickups
2. Single wharehouse
3. All parcels are available the night before the delivery
4. Static planning. Routes are planned in advanced.
