#!/usr/bin/env python
"""Mocky installer."""
from setuptools import find_packages, setup

mocked_commands = {
    'cc': 'critical',
    'cp': 'info',
    'cpio': 'info',
    'dos2unix': 'info',
    'g++': 'critical',
    'gcc': 'critical',
    'gzip': 'info',
    'install': 'error',
    'mv': 'error',
    'rm': 'debug',
    'strip': 'debug',
    'tar': 'info',
}

setup(
    name='mocky',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['coloredlogs'],
    entry_points={
        'console_scripts':
        ['{0} = mocky.__main__:{1}'.format(command, level) for command, level in mocked_commands.items()],
    }, )
