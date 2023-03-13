from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

# From position and velocity

r = [-6045, -3490, 2500] << u.km
v = [-3.457, 6.618, 2.533] << u.km / u.s

orb = Orbit.from_vectors(Earth, r, v)
# print(orb)
# print(orb.epoch)
# print(orb.epoch.iso)
# print(orb.get_frame())

"""
## From Classical Orbital Elements
"""
# Data for Mars at J2000 from JPL HORIZONS
a = 1.523679 << u.AU # semimajor axis
ecc = 0.093315 << u.one # eccentricity
inc = 1.85 << u.deg # inclination angle
raan = 49.562 << u.deg # right ascension of ascending node
argp = 286.537 << u.deg # argument of perigee
nu = 23.33 << u.deg # Trueanomaly

orb = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)
# print(orb.period.to(u.day))
# print(orb.v)

"""
## Moving forward in time: propagation
"""