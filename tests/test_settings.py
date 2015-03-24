#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
TESTS_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    "geelweb.django.contactform",
]

SITE_ID = 1

SECRET_KEY = 'aTi1Pi1EsaiJoh1O'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tests.urls'

TEMPLATE_DIRS = (
    os.path.join(TESTS_DIR, 'templates'),
)

CONTACTFORM_RECIPIENTS = ['guillaume@geelweb.org']
