#!/usr/bin/env python
from setuptools import setup

setup(
    name='3color Press',
    version='0.01',
    packages=['threecolor'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'Flask',
    'Flask-FlatPages',
    'Frozen-Flask',
    ]
)
