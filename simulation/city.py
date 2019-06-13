from model import city

class City:
    
    def __init__(self, noise_src, POIs=[], distances="square",dist_unit=("meters","m"),dist_correction_factor=1.0):
        # save Point Of Interest (e.g: WHS, MH, DP, ...)
        self._model = city.City(POIs)
        self._dist_unit = dist_unit
        self._noise_src = noise_src

    def travel_time(self, src: str, dst: str, vehicle: object) -> float:
        '''
            Computes a navigation time between 2 PointOfInterest in the city.
            The time is proportional to the distance, multiplied by a correction factor,
            and is added a noise representing traffic conditions.
        '''
        time,uncertainty = self._model.expected_travel_time(src,dst,vehicle)
        travel_time = self._noise_src.noisy_time(time,uncertainty) 
        return travel_time
