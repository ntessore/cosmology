# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""cosmology contains classes and functions for cosmological distance measures
and other cosmology-related calculations.

See the `documentation <https://cosmology.readthedocs.io>`_ for more detailed
usage examples and references.
"""

try:
    from .version import version as __version__
except ModuleNotFoundError:
    pass

from .core import *
from .funcs import *
