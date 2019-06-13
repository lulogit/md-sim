class City:
    
    def __init__(self, POIs=[], distances="square",dist_correction_factor=1.0):
        # save Point Of Interest (e.g: WHS, MH, DP, ...)
        self._poi = {
                poi_id: (p["lat"],p["lon"])
                for poi_id,p in POIs.items()}
        # some options to compute distances
        self._dist_correction_factor = dist_correction_factor

    def poi_location(self, poi_id: str):
        'Returns the location of a Point Of Interest in the city'
        return self._poi[poi_id]

    def distance(self, src: (float,float), dst: (float, float)) -> float:
        'compute the distance between 2 coordinates'
        x1,y1 = src
        x2,y2 = dst
        return (abs(x2-x1)+abs(y2-y1)) * self._dist_correction_factor

    def expected_travel_time(self, src: str, dst: str, vehicle: object) -> float:
        '''
            Computes a navigation time between 2 PointOfInterest in the city.
            The time is proportional to the distance, multiplied by a correction factor.
            It returns both the expected travel time and the uncertainty on the estimation (as tuple).
        '''
        src_loc = self.poi_location(src)
        dst_loc = self.poi_location(dst)
        dist = self.distance(src_loc, dst_loc)
        time = dist / vehicle.top_speed # time of the travel
        return (time, 0.5*time)
