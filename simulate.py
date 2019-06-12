#!/usr/bin/python3
import json
from simulation import Simulation
from simulation.config import defaults

def main(
        verbose: ("Print verbose messages","flag","vv"),
        upto: ("The simulation time in minutes","option","t",float,None,"TIME"), 
        conf: ("A .json file containing the parameters to run the simulation","option","c",str,None,"CONFIG"), 
        plan: "A .json file containing the planning for the delivery"):
    '''
        Simulate a multimodal parcel delivery in a city
    '''
    with open(plan) as plan_file:
        routes = json.load(plan_file)
        if conf:
            with open(conf) as config_file:
                params = json.load(config_file)
        else:
           params = defaults
        sim = Simulation(routes, params)
        log = sim.run(upto) if upto else sim.run()
        if verbose:
            print(log)

if __name__=="__main__":
    import plac; plac.call(main)
