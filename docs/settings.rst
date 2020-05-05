========
Settings
========

Following settings are available to customize the form

CONTACTFORM_RECIPIENTS
----------------------

Required. A list of recipients to send the message posted using the form.

Example:

.. code-block:: python

    CONTACTFORM_RECIPIENTS = ['me@example.com', 'somebody@example.com']

CONTACTFORM_SUBJECT
-------------------

Default: 'New message'

The subject of the email you'll receive when the form is posted

CONTACTFORM_MSG_TEMPLATE
------------------------

Default: 'contactform/message.txt'

The template used to render the email sent.

The following entries will be used as the template's context for rendering:

* ``site``: The current [Site](https://docs.djangoproject.com/en/3.0/ref/contrib/sites/)
* ``email``: the email field of the form
* ``phone``: the phone field of the form
* ``comment``: the comment field of the form


CONTACTFORM_FRONTEND_FRAMEWORK
------------------------------

Default: None

The front-end framework to use to render the form. Available values are

* bootstrap
* uikit
* None

If ``None`` the form will be rendered using Django stantart ``form.as_p``

If ``bootstrap`` or ``uikit`` django-widget-tweaks is required to manage css classes of input fields https://pypi.org/project/django-widget-tweaks/

CONTACTFORM_USE_THANKS_PAGE
---------------------------

Default: True

Display a confirmation page when the form is submited

CONTACTFORM_DISPLAY_FORM_TITLE
------------------------------

Default: True

Display a title before the form.
