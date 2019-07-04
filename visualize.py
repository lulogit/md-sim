#!/usr/bin/python3
import json
import time
import sys
import os

def main(
        verbose: ("Print verbose messages","flag","vv"),
        emoji: ("Print emoji log","flag","emj"),
        Json: ("Print json log","flag","json"),
        upto: ("The simulation time in minutes","option","t",float,None,"TIME"), 
        conf: ("A .json file containing the parameters to run the simulation","option","c",str,None,"CONFIG"), 
        #topo: "A .json file containing the topology of the city",
        #plan: "A .json file containing the planning (routes) for the delivery"
        ):
    '''
        Simulate a multimodal parcel delivery in a city
    '''

    web_dir = os.path.join(os.path.dirname(__file__), 'visualization/web')
    
    import subprocess
    subprocess.Popen(["/usr/bin/chromium-browser","http://127.0.0.1:8000/"])
    
    from visualization.server import start
    start(web_dir)

if __name__=="__main__":
    import plac; plac.call(main)
