# Django ContactForm Application

Display a basic contact form.

## Demo

A demo is available [here](http://django.sandbox.geelweb.org/contact)

## Installation

From PyPI

    pip install django-contactform

From Source:

	python setup.py install


## Configuration

### settings.py

Edit your settings.py file and add `geelweb.django.contactform` to the `INSTALLED_APPS`

Settings properties

*CONTACTFORM_RECIPIENTS*: list of email address the messages will be sent.

	CONTACTFORM_RECIPIENTS = [
	    'yourname@example.com',
	    'anotherperson@example.com'
	    ]

*CONTACTFORM_SUBJECT_PREFIX*: A prefix to add to the email subject

	CONTACTFORM_SUBJECT_PREFIX = 'mail from contactform'


### urls.py

Edit your urls.py and add the following line

	url(r'^contact/$', 'geelweb.django.contactform.views.contact', name='contact'),

### templates

Create a contactform/contact.html template

    <form action="{% url 'contact' %}" method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <input type="submit" value="Submit" />
	</form>

Then a contactform/thanks.html template

	<h1>Thanks for your message</h1>
	<div>Your message has been sent, we'll try to answer you as quickly as possible.</div>


### django.core.mail

Finaly check you configured django.core.mail https://docs.djangoproject.com/en/dev/topics/email/
