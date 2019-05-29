from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="ms2vec",
    version="0.0.1",
    ext_modules=cythonize("./ms2vec/word2vec_inner.pyx", compiler_directives={'language_level': 3}),
    include_dirs=[numpy.get_include()],
)
