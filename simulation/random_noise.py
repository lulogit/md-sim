import numpy as np

def set_seed(seed):
    np.random.seed(seed)

def add_noise(value, uncertainty):
    return np.random.normal(value, uncertainty)

def noisy_time(time, uncertainty):
    return max(0, add_noise(time, uncertainty))
