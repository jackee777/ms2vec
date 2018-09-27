from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="test",
    ext_modules=cythonize("word2vec_inner.pyx"),
    include_dirs=[numpy.get_include()],
)
