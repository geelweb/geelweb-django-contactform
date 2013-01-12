#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

setup(
    name="django contactform",
    version="0.1",
    description="Django Contact Form Application",
    author="Guillaume Luchet",
    author_email="guillaume@geelweb.org",
    namespace_packages = ['geelweb', 'geelweb.django'],
    packages=find_packages('src'),
    package_dir = {'':'src'},
    url="http://geelweb.org",
    )

