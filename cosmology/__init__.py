# Licensed under a 3-clause BSD style license - see LICENSE.rst
""" astropy.cosmology contains classes and functions for cosmological
distance measures and other cosmology-related calculations.

See the `Astropy documentation
<https://docs.astropy.org/en/latest/cosmology/index.html>`_ for more
detailed usage examples and references.
"""

try:
    from .version import version as __version__
except ModuleNotFoundError:
    pass

from .core import *
from .funcs import *
