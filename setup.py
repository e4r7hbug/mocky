#!/usr/bin/env python
"""Mocky installer."""
from setuptools import find_packages, setup

setup(
    name='mocky',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['coloredlogs'],
    entry_points={
        'console_scripts': [
            'cc = mocky.__main__:critical',
            'cp = mocky.__main__:info',
            'gcc = mocky.__main__:critical',
            'install = mocky.__main__:error',
            'mocky = mocky.__main__:main',
            'rm = mocky.__main__:debug',
        ],
    }, )
