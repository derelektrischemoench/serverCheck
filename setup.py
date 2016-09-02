import os
from setuptools import setup

setup(
    name='servercheck',
    version='0.1.dev0',
    description='A utility to monitor the status of websites',
    url='git@github.com:derelektrischemoench/serverCheck.git',
    author='Chris Bader',
    author_email='chris.bader@schnapptack.de',
<<<<<<< HEAD
    packages=['Mock', 'servercheck', 'tests'],
=======
    packages=['servercheck', 'tests', 'requests'],
>>>>>>> f07e30b7aca65bba70da8f085f52b562e42b7565
    install_requires=['unittest2'],
)
