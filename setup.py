from distutils.core import setup
from setuptools import find_packages
import os

setup(
    # Name of the package
    name='OLXFakedTestData',

    # Packages to include into the distribution
    packages=find_packages('.'),

    # Start with a small number and increase it with every change you make
    # https://semver.org
    version='1.0.0',

    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    # For example: MIT
    license='',

    # Short description of your library
    description='',

    # Your name
    author='Pavlo Mryhlotskyi',

    # Your email
    author_email='kozak.holota@gmail.com'
)