from skyfield.api import Topos, Loader, EarthSatellite
from skyfield.positionlib import position_of_radec
from skyfield.api import load, wgs84
import math

ts = load.timescale()
t = ts.now()

earth = 399  # NAIF code for the Earth center of mass
ra_hours = 3.79
dec_degrees = 24.1167


# returns the subpoint
def get_pleiades_pos(cent, hours, degrees):
    pleiades = position_of_radec(hours, degrees, t=t, center=cent)
    subpoint = wgs84.subpoint(pleiades)
    return subpoint


# returns latitude
def get_pleiades_lat(subpoint):
    return subpoint.latitude


# returns longitude
def get_pleiades_long(subpoint):
    return subpoint.longitude


def point_to_str(subpoint):
    return str(subpoint)


def point_arr(s):
    l = s.split(" ")
    f = []
    f.append(abs(math.cos(float(l[2]))))
    f.append(abs(math.cos(float(l[5]))))
    return f


def final_val(a):
    return a[0] * a[1]

point = get_pleiades_pos(earth, ra_hours, dec_degrees)
print(point)
print(final_val(point_arr(point_to_str(point))))
