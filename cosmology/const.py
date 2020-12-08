'''physical constants
'''

from math import pi

# Planck constant [J s]
h = 6.62607015e-34

# Boltzmann constant [J K-1]
k_B = 1.380649e-23

# Speed of light in vacuum [m s-1]
c = 299792458.

# Gravitational constant [m3 kg-1 s-2]
G = 6.67430e-11

# Stefan-Boltzmann constant [W K-4 m-2]
sigma_sb = 2 * pi**5 * k_B**4 / (15 * h**3 * c**2)

# Electron charge [C]
e = 1.602176634e-19

# Astronomical Unit [m]
au = 1.49597870700e11

# Megaparsec [m]
Mpc = 648000 / pi * au * 1e6

# Gigayear [s]
Gyr = 3600 * 24 * 365.25 * 1e9
