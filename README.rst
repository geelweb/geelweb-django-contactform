===========
ContactForm
===========

|Build status| |Documentation Status|

Django app to manage simple contact form On Django >= 3 projects.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install the app using pip

.. code-block:: text

    pip install django-contactform


2. Add 'contactform' to your `INSTALLED_APPS` settings like this

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'contactform',
    ]

3. Configure the recipients of your form in your settings

.. code-block:: python

    CONTACTFORM_RECIPIENTS = ['me@example.com']

4. Include the contactform URLconf in your project urls.py like

.. code-block:: python

    path('contact/', include('contactform.urls')),

5. Add a form to your page using the `contact_form` template tag

.. code-block:: python

    {% load contact_form %}

    {% contact_form %}


.. |Build status| image:: https://travis-ci.org/geelweb/geelweb-django-contactform.svg?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/django-contactform/badge/?version=latest
   :target: https://readthedocs.org/projects/django-contactform/?badge=latest

