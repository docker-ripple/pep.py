from __future__ import annotations

from setuptools import Extension, setup
from Cython.Build import cythonize

# List of Cython modules to build
cython_modules = [
    Extension("handlers.mainHandler", ["handlers/mainHandler.pyx"]),
    Extension("helpers.packetHelper", ["helpers/packetHelper.pyx"]),
]

# Build the Cython modules
setup(
    name="pep.py Cython modules",
    ext_modules=cythonize(cython_modules, nthreads=4),
)

