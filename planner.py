#!/usr/bin/python3
import json
import time
import model

def main(
        verbose: ("Print verbose messages","flag","vv"),
        emoji: ("Print emoji log","flag","emj"),
        output: ("Output plan to file","option","o"),
        config: ("A .json file containing planning options","option","c"), 
        fleet: "A .json file containing the parameters about the delivery system", 
        topo: "A .json file containing the topology of the city",
        orders: "A .json file containing the orders to deliver"):
    '''
        Plan the multimodal parcel delivery in a city
    '''
    with open(orders) as orders_file, open(topo) as topo_file, open(fleet) as fleet_file:
        # load planning input and parameters
        orders = json.load(orders_file)
        city = json.load(topo_file)
        fleet = json.load(fleet_file)
        # computes the Plan
        plan = {"the": "plan"}
        # outputs the plan
        if output:
            with open(output,"w") as plan_file:
                json.dump(plan, plan_file)
        else:
            print(json.dumps(plan,indent=2))

if __name__=="__main__":
    import plac; plac.call(main)
