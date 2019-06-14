from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name="ms2vec",
    version="0.1.0",
    ext_modules=cythonize("./ms2vec/ms2vec_inner.pyx", compiler_directives={'language_level': 3}),
    include_dirs=[np.get_include()],
)
