from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="ms2vec",
    version="0.0.1",
    #ext_modules=cythonize("word2vec_inner.pyx"),
    include_dirs=[numpy.get_include()],
)
