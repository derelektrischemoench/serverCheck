import os
from setuptools import setup

setup(
    name='servercheck',
    version='0.1dev',
    description='A utility to monitor the status of websites',
    url='git@github.com:derelektrischemoench/serverCheck.git',
    author='Chris Bader',
    author_email='chris.bader@schnapptack.de',
    packages=['servercheck', 'tests', 'requests'],
    install_requires=['unittest2'],
)
