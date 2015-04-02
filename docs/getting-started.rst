Getting Started
===============

Installation
------------

1. Install latest stable version from PyPi:

.. code-block:: text

    $ pip install geelweb-django-contactform

2. Add `geelweb.django.contactform` to ``INSTALLED_APPS`` in your project settings

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'geelweb.django.contactform',,
    )

3. Include the contactform urls in your project `urls.py`

.. code-block:: python

	url(r'^contact/$', 'geelweb.django.contactform.views.contact', name='contact'),

Create templates
----------------

Create 2 templates to display the form and the confirmation page displayed when
the form has been posted

1. The contact form template in `contactform/contact.html`

.. code-block:: html

    <form action="{% url 'contact' %}" method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <input type="submit" value="Submit" />
	</form>

2. The confirmation template in `contactform/thanks.html`

.. code-block:: html

	<h1>Thanks for your message</h1>
	<div>Your message has been sent, we'll try to answer you as quickly as possible.</div>

Configure settings
------------------

1. Configure `django.core.mail` as explained in the Django documentation
   https://docs.djangoproject.com/en/dev/topics/email/

2. Configure `geelweb.django.contactform` adding the recipients in your project settings

.. code-block:: python

    CONTACTFORM_RECIPIENTS = ['email@example.com']

You can discover all available settings in the :doc:`settings`

Test
----

Start the development server and visit http://127.0.0.1/contact/ to view the
contact form
