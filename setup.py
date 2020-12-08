from setuptools import setup
from Cython.Build import cythonize

setup(
    use_scm_version={
        'write_to': 'cosmology/version.py',
    },
    ext_modules=cythonize('cosmology/scalar_inv_efuncs.pyx'),
)
