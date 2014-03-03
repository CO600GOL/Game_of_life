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
    packages=find_packages() + packages,
    install_requires=requires,
    license='MIT',
)
