from setuptools import setup, find_packages

setup(
    name='settling_parameter_estimation',
    version='0.1',
    packages=find_packages(include=['src', 'src.*', 'utils', 'utils.*', 'scripts']),
)