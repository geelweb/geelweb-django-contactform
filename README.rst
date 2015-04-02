Django ContactForm Application
==============================

|Build status| |Documentation Status|

Display a basic contact form.

Demo
----

A demo is available `here`_

Installation
------------

From PyPI

.. code-block:: text

    pip install django-contactform

From Source:

.. code-block:: text

    python setup.py install

Configuration
-------------

settings.py
~~~~~~~~~~~

Edit your settings.py file and add ``geelweb.django.contactform`` to the
``INSTALLED_APPS``

Settings properties

*CONTACTFORM\_RECIPIENTS*: list of email address the messages will be
sent.

.. code-block:: python

    CONTACTFORM_RECIPIENTS = [
        'yourname@example.com',
        'anotherperson@example.com'
        ]

*CONTACTFORM\_SUBJECT\_PREFIX*: A prefix to add to the email subject

.. code-block:: python

    CONTACTFORM_SUBJECT_PREFIX = 'mail from contactform'

urls.py
~~~~~~~

Edit your urls.py and add the following line

.. code-block:: python

    url(r'^contact/$', 'geelweb.django.contactform.views.contact', name='contact'),

templates
~~~~~~~~~

Create a contactform/contact.html template

.. code-block:: html

    <form action="{% url 'contact' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit" />
    </form>

Then a contactform/thanks.html template

.. code-block:: html

    <h1>Thanks for your message</h1>
    <div>Your message has been sent, we'll try to answer you as quickly as possible.</div>

django.core.mail
~~~~~~~~~~~~~~~~

Finaly check you configured django.core.mail
https://docs.djangoproject.com/en/dev/topics/email/

Testing
-------

Run unit-tests

.. code-block:: text

    python tests/runtests.py

.. _here: http://django.sandbox.geelweb.org/contact

.. |Build status| image:: https://travis-ci.org/geelweb/geelweb-django-contactform.svg?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/django-contactform/badge/?version=latest
   :target: https://readthedocs.org/projects/django-contactform/?badge=latest
