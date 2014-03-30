from setuptools import setup, find_packages

requires = [
    "pytest",
    "pytest-cov"
    ]

packages = [
    "game",
    "game_of_life"
    ]

# Information to add to the package during setup
setup(
    name='GameOfLife',
    version='1.0',
    packages=packages + find_packages(),
    install_requires=requires,
    license='MIT',
)
