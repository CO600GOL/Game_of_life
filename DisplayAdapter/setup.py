from setuptools import setup, find_packages

# The requires for the DisplayAdapter setup
requires = [
    "pytest",
    "pytest-cov",
    "mock"
]

# The packages required for the DisplayAdapter setup
packages = [
    "display_adapter",
    "serial"
]

# The information to add on setup of the application
setup(
    name='DisplayAdapter',
    version='1.1',
    packages=packages + find_packages(),
    install_requires=requires,
    license='MIT',
)
