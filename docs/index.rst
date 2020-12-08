***************************************
Cosmological Calculations (`cosmology`)
***************************************

Introduction
============

The `cosmology` package contains classes for representing
cosmologies and utility functions for calculating commonly used
quantities that depend on a cosmological model. This includes
distances, ages, and lookback times corresponding to a measured
redshift or the transverse separation corresponding to a measured
angular separation.


Getting Started
===============

Cosmological quantities are calculated using methods of a
:class:`~cosmology.Cosmology` object.

Examples
--------

..
  EXAMPLE START
  Calculating Cosmological Quantities

To calculate the Hubble constant at z=0 (i.e., ``H0``) and the number of
transverse proper kiloparsecs (kpc) corresponding to an arcminute at z=3::

  >>> from cosmology import WMAP9 as cosmo
  >>> cosmo.H(0)
  69.32

  >>> cosmo.kpc_proper_per_arcmin(3)  # doctest: +ELLIPSIS
  472.977...

Here WMAP9 is a built-in object describing a cosmology with the
parameters from the nine-year WMAP results. Several other built-in
cosmologies are also available (see `Built-in Cosmologies`_). The
available methods of the cosmology object are listed in the methods
summary for the :class:`~cosmology.FLRW` class. If you are using
IPython you can also use tab completion to print a list of the
available methods. To do this, after importing the cosmology as in the
above example, type ``cosmo.`` at the IPython prompt and then press
the tab key.

All of these methods also accept an arbitrarily-shaped array of
redshifts as input::

  >>> from cosmology import WMAP9 as cosmo
  >>> cosmo.comoving_distance([0.5, 1.0, 1.5])  # doctest: +ELLIPSIS
  array([1916.06..., 3363.07..., 4451.74...])

You can create your own FLRW-like cosmology using one of the cosmology
classes::

  >>> from cosmology import FlatLambdaCDM
  >>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)
  >>> cosmo
  FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725, Neff=3.04, m_nu=[0. 0. 0.], Ob0=None)

Note the presence of additional cosmological parameters (e.g., ``Neff``,
the number of effective neutrino species) with default values; these
can also be specified explicitly in the call to the constructor.

..
  EXAMPLE END


Using `cosmology`
=================

Most of the functionality is enabled by the :class:`~cosmology.FLRW`
object. This represents a homogeneous and isotropic cosmology
(characterized by the Friedmann-Lemaitre-Robertson-Walker metric,
named after the people who solved Einstein's field equation for this
special case). However, you cannot work with this class directly, as
you must specify a dark energy model by using one of its subclasses
instead, such as :class:`~cosmology.FlatLambdaCDM`.

Examples
--------

..
  EXAMPLE START
  Working with the FlatLambdaCDM Class

You can create a new :class:`~cosmology.FlatLambdaCDM` object with
arguments giving the Hubble parameter and Omega matter (both at z=0)::

  >>> from cosmology import FlatLambdaCDM
  >>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
  >>> cosmo
  FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=0, Neff=3.04, m_nu=None, Ob0=None)

The predefined cosmologies described in the `Getting Started`_
section are instances of :class:`~cosmology.FlatLambdaCDM`, and have
the same methods. So we can find the luminosity distance to
redshift 4 by::

  >>> cosmo.luminosity_distance(4)  # doctest: +ELLIPSIS
  35851.8...

Or the age of the universe at z = 0::

  >>> cosmo.age(0)  # doctest: +ELLIPSIS
  13.4669...

They also accept arrays of redshifts::

  >>> cosmo.age([0.5, 1, 1.5])  # doctest: +ELLIPSIS
  array([8.42634..., 5.75164..., 4.20073...])

See the :class:`~cosmology.FLRW` and :class:`~cosmology.FlatLambdaCDM` object
docstring for all of the methods and attributes available.

..
  EXAMPLE END

..
  EXAMPLE START
  Working with Non-flat Universes with the LambdaCDM Class

In addition to flat universes, non-flat varieties are supported, such as
:class:`~cosmology.LambdaCDM`. A variety of standard cosmologies with the
parameters already defined are also available
(see `Built-in Cosmologies`_)::

  >>> from cosmology import WMAP7   # WMAP 7-year cosmology
  >>> WMAP7.critical_density(0)  # critical density at z = 0  # doctest: +ELLIPSIS
  9.30936...e-30

You can see how the density parameters evolve with redshift as well::

  >>> from cosmology import WMAP7   # WMAP 7-year cosmology
  >>> WMAP7.Om([0, 1.0, 2.0]), WMAP7.Ode([0., 1.0, 2.0])  # doctest: +ELLIPSIS
  (array([0.272..., 0.748..., 0.909...]), array([0.727..., 0.250..., 0.090...]))

Note that these do not quite add up to one, even though WMAP7 assumes a
flat universe, because photons and neutrinos are included.

It is possible to specify the baryonic matter density at redshift zero
at class instantiation by passing the keyword argument ``Ob0``::

  >>> from cosmology import FlatLambdaCDM
  >>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Ob0=0.05)
  >>> cosmo
  FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=0, Neff=3.04, m_nu=None, Ob0=0.05)

In this case the dark matter-only density at redshift 0 is
available as class attribute ``Odm0`` and the redshift evolution of
dark and baryonic matter densities can be computed using the methods
``Odm`` and ``Ob``, respectively. If ``Ob0`` is not specified at class
instantiation, it defaults to ``None`` and any method relying on it
being specified will raise a ``ValueError``::

  >>> from cosmology import FlatLambdaCDM
  >>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
  >>> cosmo.Odm(1)
  Traceback (most recent call last):
  ...
  ValueError: Baryonic density not set for this cosmology, unclear meaning of dark matter density

Cosmological instances have an optional ``name`` attribute which can be
used to describe the cosmology::

  >>> from cosmology import FlatwCDM
  >>> cosmo = FlatwCDM(name='SNLS3+WMAP7', H0=71.58, Om0=0.262, w0=-1.016)
  >>> cosmo
  FlatwCDM(name="SNLS3+WMAP7", H0=71.6, Om0=0.262, w0=-1.02, Tcmb0=0, Neff=3.04, m_nu=None, Ob0=None)

..
  EXAMPLE END

This is also an example with a different model for dark energy: a flat
universe with a constant dark energy equation of state, but not
necessarily a cosmological constant. A variety of additional dark
energy models are also supported (see `Specifying a dark energy
model`_).

An important point is that the cosmological parameters of each
instance are immutable — that is, if you want to change, say,
``Om``, you need to make a new instance of the class. To make
this more convenient, a ``clone`` operation is provided, which
allows you to make a copy with specified values changed.
Note that you cannot change the type of cosmology with this operation
(e.g., flat to non-flat).

..
  EXAMPLE START
  Making New Cosmology Instances with the .clone() Method

To make a copy of a cosmological instance using the ``clone`` operation::

  >>> from cosmology import WMAP9
  >>> newcosmo = WMAP9.clone(name='WMAP9 modified', Om0=0.3141)
  >>> WMAP9.H0, newcosmo.H0  # some values unchanged
  (69.32, 69.32)
  >>> WMAP9.Om0, newcosmo.Om0  # some changed
  (0.2865, 0.3141)
  >>> WMAP9.Ode0, newcosmo.Ode0  # Indirectly changed since this is flat  # doctest: +ELLIPSIS
  (0.713413..., 0.685813...)

..
  EXAMPLE END

Finding the Redshift at a Given Value of a Cosmological Quantity
----------------------------------------------------------------

If you know a cosmological quantity and you want to know the
redshift which it corresponds to, you can use ``z_at_value``.

Example
^^^^^^^

..
  EXAMPLE START
  Compute the Redshift at a Given Universe Age

To find the redshift when the universe was 2 Gyr old using ``z_at_value``::

  >>> from cosmology import Planck13, z_at_value
  >>> z_at_value(Planck13.age, 2.)  # doctest: +ELLIPSIS
  3.19812...

..
  EXAMPLE END

For some quantities, there can be more than one redshift that satisfies
a value. In this case you can use the ``zmin`` and ``zmax`` keywords
to restrict the search range. See the ``z_at_value`` docstring for more
detailed usage examples.


Built-in Cosmologies
--------------------

A number of preloaded cosmologies are available from analyses using
the WMAP and Planck satellite data. For example::

  >>> from cosmology import Planck13  # Planck 2013
  >>> Planck13.lookback_time(2)  # lookback time in Gyr at z=2  # doctest: +ELLIPSIS
  10.5118...

A full list of the predefined cosmologies is given by
``cosmology.parameters.available`` and summarized below:

========  ============================== ====  ===== =======
Name      Source                         H0    Om    Flat
========  ============================== ====  ===== =======
WMAP5     Komatsu et al. 2009            70.2  0.277 Yes
WMAP7     Komatsu et al. 2011            70.4  0.272 Yes
WMAP9     Hinshaw et al. 2013            69.3  0.287 Yes
Planck13  Planck Collab 2013, Paper XVI  67.8  0.307 Yes
Planck15  Planck Collab 2015, Paper XIII 67.7  0.307 Yes
Planck18  Planck Collab 2018, Paper VI   67.7  0.310 Yes
========  ============================== ====  ===== =======

.. note::

  Unlike the Planck 2015 paper, the Planck 2018 paper includes massive
  neutrinos in ``Om0`` but the Planck18 object includes them in ``m_nu`` instead
  for consistency. Hence, the ``Om0`` value in Planck18 differs slightly
  from the Planck 2018 paper but represents the same cosmological model.

Currently, all are instances of :class:`~cosmology.FlatLambdaCDM`.
More details about exactly where each set of parameters comes from
are available in the docstring for each object::

  >>> from cosmology import WMAP7
  >>> print(WMAP7.__doc__)
  WMAP7 instance of FlatLambdaCDM cosmology
  <BLANKLINE>
  (from Komatsu et al. 2011, ApJS, 192, 18, doi: 10.1088/0067-0049/192/2/18. Table 1 (WMAP + BAO + H0 ML).)


Specifying a Dark Energy Model
------------------------------

Along with the standard :class:`~cosmology.FlatLambdaCDM` model
described above, a number of additional dark energy models are
provided. :class:`~cosmology.FlatLambdaCDM`
and :class:`~cosmology.LambdaCDM` assume that dark
energy is a cosmological constant, and should be the most commonly
used cases; the former assumes a flat universe, the latter allows
for spatial curvature. :class:`~cosmology.FlatwCDM` and
:class:`~cosmology.wCDM` assume a constant dark
energy equation of state parameterized by :math:`w_{0}`.
Two forms of a variable dark energy equation of state are provided: the simple
first order linear expansion :math:`w(z) = w_{0} + w_{z} z` by
:class:`~cosmology.w0wzCDM`, as well as the common CPL form by
:class:`~cosmology.w0waCDM`: :math:`w(z) = w_{0} + w_{a} (1 - a) =
w_{0} + w_{a} z / (1 + z)` and its generalization to include a pivot
redshift by :class:`~cosmology.wpwaCDM`: :math:`w(z) = w_{p} + w_{a}
(a_{p} - a)`.

Users can specify their own equation of state by subclassing
:class:`~cosmology.FLRW`. See the provided subclasses for
examples. It is recommended, but not required, that all arguments to the
constructor of a new subclass be available as properties, since the
``clone`` method assumes this is the case. It is also advisable
to stick to subclassing :class:`~cosmology.FLRW` rather than one of
its subclasses, since some of them use internal optimizations that
also need to be propagated to any subclasses. Users wishing to
use similar tricks (which can make distance calculations much faster)
should consult the cosmology module source code for details.

Photons and Neutrinos
---------------------

The cosmology classes (can) include the contribution to the energy density
from both photons and neutrinos. By default, the latter are assumed
massless. The three parameters controlling the properties of these
species, which are arguments to the initializers of all of the
cosmological classes, are ``Tcmb0`` (the temperature of the cosmic microwave
background at z=0), ``Neff`` (the effective number of neutrino species), and
``m_nu`` (the rest mass of the neutrino species). ``Tcmb0`` and ``m_nu`` should
be expressed as unit Quantities. All three have standard default values — 0 K,
3.04, and 0 eV, respectively. (The reason that ``Neff`` is not 3 has to do
primarily with a small bump in the neutrino energy spectrum due to electron-
positron annihilation, but is also affected by weak interaction physics.)
Setting the CMB temperature to 0 removes the contribution of both neutrinos and
photons. This is the default to ensure these components are excluded unless the
user explicitly requests them.

Massive neutrinos are treated using the approach described in the
WMAP seven-year cosmology paper (Komatsu et al. 2011, ApJS, 192, 18, section
3.3). This is not the simple
:math:`\Omega_{\nu 0} h^2 = \sum_i m_{\nu\, i} / 93.04\,\mathrm{eV}`
approximation. Also note that the values of :math:`\Omega_{\nu}(z)`
include both the kinetic energy and the rest mass energy components,
and that the Planck13 and Planck15 cosmologies include a single
species of neutrinos with non-zero mass (which is not included in
:math:`\Omega_{m0}`).

Adding massive neutrinos can have significant performance implications.
In particular, the computation of distance measures and lookback times
are factors of three to four times slower than in the massless neutrino case.
Therefore, if you need to compute many distances in such a cosmology and
performance is critical, it is particularly useful to calculate them on
a grid and use interpolation.

Examples
^^^^^^^^

..
  EXAMPLE START
  Calculating the Contribution of Photons and Neutrinos to the Energy Density

The contribution of photons and neutrinos to the total mass-energy density
can be found as a function of redshift::

  >>> from cosmology import WMAP7   # WMAP 7-year cosmology
  >>> WMAP7.Ogamma0, WMAP7.Onu0  # Current epoch values  # doctest: +ELLIPSIS
  (4.98603...e-05, 3.44239...e-05)
  >>> z = [0, 1.0, 2.0]
  >>> WMAP7.Ogamma(z), WMAP7.Onu(z)  # doctest: +ELLIPSIS
  (array([4.98603...e-05, 2.74593...e-04, 4.99915...e-04]), array([3.44239...e-05, 1.89580...e-04, 3.45145...e-04]))

If you want to exclude photons and neutrinos from your calculations, you can
set ``Tcmb0`` to 0 (which is also the default)::

  >>> from cosmology import FlatLambdaCDM
  >>> cos = FlatLambdaCDM(70.4, 0.272, Tcmb0 = 0.0)
  >>> cos.Ogamma0, cos.Onu0
  (0.0, 0.0)

You can include photons but exclude any contributions from neutrinos by
setting ``Tcmb0`` to be non-zero (2.725 K is the standard value for our
Universe) but setting ``Neff`` to 0::

  >>> from cosmology import FlatLambdaCDM
  >>> cos = FlatLambdaCDM(70.4, 0.272, Tcmb0=2.725, Neff=0)
  >>> cos.Ogamma([0, 1, 2])  # Photons are still present  # doctest: +ELLIPSIS
  array([4.98603...e-05, 2.74642...e-04, 5.00086...e-04])
  >>> cos.Onu([0, 1, 2])  # But not neutrinos
  array([0., 0., 0.])

The number of neutrino species is assumed to be the floor of ``Neff``,
which in the default case is ``Neff=3``. Therefore, if non-zero neutrino masses
are desired, then three masses should be provided. However, if only one
value is provided, all of the species are assumed to have the same mass.
``Neff`` is assumed to be shared equally between each species.

::

  >>> from cosmology import FlatLambdaCDM
  >>> H0 = 70.4
  >>> m_nu = 0
  >>> cosmo = FlatLambdaCDM(H0, 0.272, Tcmb0=2.725, m_nu=m_nu)
  >>> cosmo.has_massive_nu
  False
  >>> cosmo.m_nu
  array([0., 0., 0.])
  >>> m_nu = [0.0, 0.05, 0.10]
  >>> cosmo = FlatLambdaCDM(H0, 0.272, Tcmb0=2.725, m_nu=m_nu)
  >>> cosmo.has_massive_nu
  True
  >>> cosmo.m_nu
  array([0.  , 0.05, 0.1 ])
  >>> cosmo.Onu([0, 1.0, 15.0])  # doctest: +ELLIPSIS
  array([0.003270..., 0.008968..., 0.012579...])
  >>> cosmo.Onu(1) * cosmo.critical_density(1)  # doctest: +ELLIPSIS
  2.44438...e-31

While these examples used :class:`~cosmology.FlatLambdaCDM`,
the above examples also apply for all of the other cosmology classes.

..
  EXAMPLE END

See Also
========

* Hogg, "Distance measures in cosmology",
  https://arxiv.org/abs/astro-ph/9905116
* Linder, "Exploring the Expansion History of the Universe", https://arxiv.org/abs/astro-ph/0208512
* NASA's Legacy Archive for Microwave Background Data Analysis,
  https://lambda.gsfc.nasa.gov/

Range of Validity and Reliability
=================================

The code in this package is tested against several widely used
online cosmology calculators and has been used to perform many
calculations in refereed papers. You can check the range of redshifts
over which the code is regularly tested in the module
``cosmology.tests.test_cosmology``. If you find any bugs,
please let us know by `opening an issue at the GitHub repository
<https://github.com/ntessore/cosmology/issues>`_!

A more difficult question is the range of redshifts over which
the code is expected to return valid results. This is necessarily
model-dependent, but in general you should not expect the numeric
results to be well behaved for redshifts more than a few times
larger than the epoch of matter-radiation equality (so, for typical
models, not above z = 5-6,000, but for some models much lower redshifts
may be ill-behaved). In particular, you should pay attention to warnings
from the ``scipy`` integration package about integrals failing to converge
(which may only be issued once per session).

The built-in cosmologies use the parameters as listed in the
respective papers. These provide only a limited range of precision,
and so you should not expect derived quantities to match beyond
that precision. For example, the Planck 2013 and 2015 results only provide the
Hubble constant to four digits. Therefore, they should not be expected
to match the age quoted by the Planck team to better than that, despite
the fact that five digits are quoted in the papers.

Reference/API
=============

.. currentmodule:: cosmology

Functions
---------

.. autosummary::
   :toctree: api

   z_at_value

Classes
-------

.. autosummary::
   :toctree: api

   FLRW
   FlatLambdaCDM
   Flatw0waCDM
   FlatwCDM
   LambdaCDM
   w0waCDM
   w0wzCDM
   wCDM
   wpwaCDM
