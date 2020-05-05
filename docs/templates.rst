=========
Templates
=========

Base template
-------------

All views templates extends the ``contactform/base.html`` template. Create this template in your project with a ``content`` block to update the pages layout.

.. code-block:: html

    {% extends "base.html" %}

    {% block content %}{% endblock %}

View templates
--------------

Contact page
~~~~~~~~~~~~

You can customize the contact page creating a ``contactform/contact.html`` template in your project

.. code-block:: html

    {% extends "contactform/base.html" %}
    {% load contact_form %}

    {% block content %}
      <h1>Contact</h1>

      <section>
        <address>
          42 plop street
          xxx City
        </address>
      <section>

      <section>
        {% contact_form form %}
      </section>
    {% endblock %}

Thanks page
~~~~~~~~~~~

Update the page displayed when the form is submited creating a ``contactform/thanks.html`` template in your project

Form templates
--------------

The templates used by the ``contact_form`` template tags depends of the ``CONTACTFORM_FRONTEND_FRAMEWORK`` settings, depending of it's value you can customize the form rendering creating one of the following template

* ``contactform/form.html``
* ``contactform/form_bootstrap.html``
* ``contactform/form_uikit.html``

.. code-block:: html


    <form method="POST" action="{% url 'contactform:index' %}">
      {% csrf_token %}
      {{ form.as_table }}
      <button type="submit">{% trans "Submit" %}</button>
    </form>

