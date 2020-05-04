============
Installation
============

You can install django-contactform with pip::

  pip install django-contactform

Requirements
------------

*messages framework*

Ensure the Django messages framework is enabled on your project https://docs.djangoproject.com/en/3.0/ref/contrib/messages/

*django-widget-tweaks*

django-widget-tweaks is required to manage css classes of input fields https://pypi.org/project/django-widget-tweaks/


Enable the app
--------------

1. Add 'contactform' to your `INSTALLED_APPS` settings::

    INSTALLED_APPS = [
        ...
       'widget_tweaks',
       'contactform',
    ]

3. Configure the recipients of your form in your settings::

   CONTACTFORM_RECIPIENTS = ['me@example.com']

4. Include the contactform URLconf in your project urls.py like::

   path('contact/', include('contactform.urls')),

5. Add a form to an existing page using the `contact_form` template tag::

   {% load contact_form %}

   {% contact_form %}

or add a link to the contact page::

   <a href="{% url 'contactform:index' %}">Contact us</a>

