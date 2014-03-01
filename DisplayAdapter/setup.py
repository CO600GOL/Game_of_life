from setuptools import setup, find_packages

requires = [
    "display_adapter",
    "pytest"
]

setup(
    name='DisplayAdapter',
    version='0.1',
    packages=find_packages(),
    install_requires=requires,
    license='MIT',
)
