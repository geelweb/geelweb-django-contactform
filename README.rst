===========
ContactForm
===========

|Build status| |Documentation Status|

Django app to manage simple contact form

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install the app using pip::

   pip install django-contactform

Additionaly you have to install [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)


2. Add 'contactform' and 'widget_tweaks' to your `INSTALLED_APPS` settings like this::

   INSTALLED_APPS = [
       ...
       'widget_tweaks',
       'contactform',
   ]

3. Configure the recipients of your form in your settings::

   CONTACTFORM_RECIPIENTS = ['me@example.com']

4. Include the contactform URLconf in your project urls.py like::

   path('contact/', include('contactform.urls')),

5. Add a form to your page using the `contact_form` template tag::

   {% load contact_form %}

   {% contact_form %}

.. |Build status| image:: https://travis-ci.org/geelweb/geelweb-django-contactform.svg?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/django-contactform/badge/?version=latest
   :target: https://readthedocs.org/projects/django-contactform/?badge=latest

