from setuptools import setup, find_packages

requires = [
    "pytest",
    "mock"
]

packages = [
    "display_adapter",
    "serial"
]

setup(
    name='DisplayAdapter',
    version='1.0',
    packages=packages + find_packages(),
    install_requires=requires,
    license='MIT',
)
