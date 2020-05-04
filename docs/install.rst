============
Installation
============

You can install django-contactform with pip

.. code-block:: text

    pip install django-contactform

Requirements
------------

*messages framework*

Ensure the Django messages framework is enabled on your project https://docs.djangoproject.com/en/3.0/ref/contrib/messages/


Enable the app
--------------

1. Add 'contactform' to your `INSTALLED_APPS` settings

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

5. Add a form to an existing page using the `contact_form` template tag

.. code-block:: python

    {% load contact_form %}

    {% contact_form %}


or add a link to the contact page

.. code-block:: html

    <a href="{% url 'contactform:index' %}">Contact us</a>

