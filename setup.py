#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages


setup(
    name = 'foreveryoungclinic',
    version = '0.1',
    packages = find_packages(
        exclude = ['ez_setup', 'examples', 'tests']),
)
