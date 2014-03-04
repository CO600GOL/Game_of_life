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
    version='0.1',
    packages=packages,
    install_requires=requires,
    license='MIT',
)
