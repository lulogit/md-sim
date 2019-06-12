from simulation import Simulation

def test_single_delivery():
    # plan for the delivery: urban pallets composition, vans' routes, bikers' routes
    plan = {
            "SUPs": {
                "SUP_001": ["PC_001"]
            },
            "TVs": {
                "TV_001": [
                    {   
                        "stop":"WHS", "drop":[], "take":["SUP_001"]},
                    {   
                        "stop": "MH_001", "drop":["SUP_001"], "take":[]},
                    {
                        "stop": "MH_001", "drop":[], "take":["SUP_001"]},
                    {
                        "stop": "WHS", "drop":["SUP_001"], "take":[]}
                ]
            },
            "PVs": {
                "PV_001": [
                    {
                        "stop": "MH_001", "drop": [], "take": ["SUP_001"]},
                    {
                        "stop": "DP_001", "drop": ["PC_001"], "take": []},
                    {
                        "stop": "MH_001", "drop": ["SUP_001"], "take": []}
                    ]
                }
            }
    seed = 123456789 # to generate always the same pseudo-random numbers
    sim = Simulation(plan, {})
    log = sim.run(seed)
    assert log != []
    assert len(log) is 7
