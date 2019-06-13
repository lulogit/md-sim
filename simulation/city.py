import numpy as np

class City:
    
    def __init__(self, POIs=[], distances="square",dist_unit=("meters","m"),dist_correction_factor=1.0):
        # save Point Of Interest (e.g: WHS, MH, DP, ...)
        self._poi = [
                (p["lat"],p["lon"])
                for p in POIs]
        # some options to compute distances
        self._dist_unit = dist_unit
        self._dist_correction_factor = dist_correction_factor

    def poi_location(self, poi_id: str):
        'Returns the location of a Point Of Interest in the city'
        return self._poi[poi_id]

    def distance(slef, src: (float,float), dst: (float, float)) -> float:
        'compute the distance between 2 coordinates'
        x1,y1 = src
        x2,y2 = dst
        return (abs(x2-x1)+abs(y2-y1)) * self._dist_correction_factor

    def travel_time(self, src: str, dst: str, vehicle: object) -> float:
        '''
            Computes a navigation time between 2 PointOfInterest in the city.
            The time is proportional to the distance, multiplied by a correction factor,
            and is added a noise representing traffic conditions.
        '''
        src_loc = self.poi_location(src)
        dst_loc = self.poi_location(dst)
        dist = self.distance(src_loc, dst_loc)
        time = dist / vehicle.top_speed # time of the travel
        travel_time = max(0, np.random.normal(time, 0.5*time)) # emulate traffic noise
        return travel_time
