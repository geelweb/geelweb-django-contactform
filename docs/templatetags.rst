=============
Template tags
=============

The ``contact_form`` template tags can be used to render the form in any
template.

Display a new form
------------------

.. code-block:: html

    {% contact_form %}

The template will create a ``ContactForm`` form and render it.

Display an existing form
------------------------

.. code-block:: html

    {% contact_form form %}

In case you already have a ``form`` in the template context you can add it in
argument of the ``contact_form`` tag.

Keyword arguments
-----------------

*next*:

Specify the url where redirect when the form is posted and validated

.. code-block:: html

    {% contact_form next="/my-link" %}

