import numpy as np

def car(env, name):
    while True:
        print('%s: Start parking at %d' % (name,env.now))
        parking_duration = max(0,np.random.normal(5,2))
        yield env.timeout(parking_duration)

        print('%s: Start driving at %d' % (name,env.now))
        trip_duration = max(0,np.random.normal(2,0.5))
        yield env.timeout(trip_duration)

if __name__=="__main__":
    import simpy
    env = simpy.Environment()
    env.process(car(env,"Luca"))
    env.process(car(env,"Giulio"))
    env.run(until=100)
