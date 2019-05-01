from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="MS2vec",
    ext_modules=cythonize("MultiSense2vec_inner.pyx"),
    include_dirs=[numpy.get_include()],
)
