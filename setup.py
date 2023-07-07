from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    name="module_ex",
    sources=["fichier_ex.pyx"],
)
setup(
    name="module_ex",
    ext_modules=cythonize([examples_extension])
)