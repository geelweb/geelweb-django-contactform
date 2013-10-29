# Django ContactForm Application

## Demo

A demo is available [here](http://django-sandbox.geelweb.org/contact)

## Installation

From PyPI

    pip install django-contactform

From Source:

	python setup.py install


## Configuration

### settings.py

Edit your settings.py file and add the following line into your INSTALLED_APPS

	'geelweb.django.contactform'

Then define the following configuration properties

	CONTACTFORM_RECIPIENTS = [
	    'yourname@example.com',
	    'anotherperson@example.com'
	    ]

	CONTACTFORM_SUBJECT_PREFIX = 'mail from contactform'


### urls.py

Edit your urls.py and add the following line

	url(r'^contact$', 'geelweb.django.contactform.views.contact', name='contact'),

### templates

Create a contactform/contact.html template

    <form action="{% url contact %}" method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <input type="submit" value="Submit" />
	</form>

Then a contactform/thanks.html template

	<h1>Thanks for your message</h1>
	<div>Your message has been sent, we'll try to answer you as quickly as possible.</div>


### django.core.mail

Finaly check you configured django.core.mail https://docs.djangoproject.com/en/dev/topics/email/
