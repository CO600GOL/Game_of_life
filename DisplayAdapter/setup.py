from setuptools import setup, find_packages

requires = [
    "pytest",
    "pySerial",
    "mock"
]

packages = [
    "display_adapter"
]

setup(
    name='DisplayAdapter',
    version='1.0',
    packages=packages,
    install_requires=requires,
    license='MIT',
)
