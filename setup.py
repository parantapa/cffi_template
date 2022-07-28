from setuptools import setup

setup(
    cffi_modules=["src/cffi_test/pi_extension_build.py:ffibuilder"]
)
