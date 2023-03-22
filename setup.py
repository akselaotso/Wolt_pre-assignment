from setuptools import (setup, find_packages)

setup(
    name = 'delivery_cost_calculator',
    version='1.0',
    packages = find_packages(),
    install_requires=['Flask', 'twilio', 'pytest', 'coverage']
)

