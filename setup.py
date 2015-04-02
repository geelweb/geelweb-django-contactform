#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"
__version__ = "0.2.1"

import os, sys
from setuptools import setup, find_packages

author_data = __author__.split(" ")
maintainer = " ".join(author_data[0:-1])
maintainer_email = author_data[-1]
README = open("README.rst").read()

setup(
    name="django-contactform",
    version=__version__,
    description="Django Contact Form Application",
    long_description=README,
    author=maintainer,
    author_email=maintainer_email,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url="https://github.com/geelweb/geelweb-django-contactform",
    download_url="https://github.com/geelweb/geelweb-django-contactform/tarball/%s" % __version__,
    license="MIT",
    namespace_packages = ["geelweb", "geelweb.django"],
    packages=find_packages("src"),
    package_dir={"":"src"},
    package_data = {
        'geelweb.django.contactform': [
            'locale/*/LC_MESSAGES/*.po',
            'locale/*/LC_MESSAGES/*.mo'
        ],
    },
    keywords=['django', 'contact', 'form']
)

