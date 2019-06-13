import time
import datetime


TICKS_PER_SECOND = 1

def minutes(n: float) -> float:
    'minutes to simulation ticks'
    return n * 60 * TICKS_PER_SECOND

def seconds(n: float) -> float:
    'seconds to simulation ticks'
    return n * TICKS_PER_SECOND

def as_clock(t: float) -> str:
    'represent the simulation time as clock: hh:mm[:ss]'
    ss = int(t / TICKS_PER_SECOND)
    mm = (ss // 60) % 60
    hh = ss // 3600
    return "%02d:%02d" % (hh,mm)
