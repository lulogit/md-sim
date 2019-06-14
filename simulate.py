#!/usr/bin/python3
import json
import time
from simulation import Simulation
from simulation.config import defaults
from simulation.logging import render

def main(
        verbose: ("Print verbose messages","flag","vv"),
        upto: ("The simulation time in minutes","option","t",float,None,"TIME"), 
        conf: ("A .json file containing the parameters to run the simulation","option","c",str,None,"CONFIG"), 
        topo: "A .json file containing the topology of the city",
        plan: "A .json file containing the planning (routes) for the delivery"):
    '''
        Simulate a multimodal parcel delivery in a city
    '''
    with open(plan) as plan_file, open(topo) as topo_file:
        routes = json.load(plan_file)
        city = json.load(topo_file)
        if conf:
            with open(conf) as config_file:
                params = json.load(config_file)
        else:
           params = defaults
        seed = int(time.time())
        sim = Simulation(routes, city, params)
        log = sim.run(seed, upto) if upto else sim.run(seed)
        if verbose:
            render(log)

if __name__=="__main__":
    import plac; plac.call(main)
