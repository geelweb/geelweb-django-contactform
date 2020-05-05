from django import template
from django.conf import settings

from contactform.forms import ContactForm

register = template.Library()

@register.inclusion_tag('contactform/tags/contact_form.html', takes_context=True)
def contact_form(context, form=None, *args, **kwargs):
    if form is None:
        next_url = kwargs['next'] if 'next' in kwargs else None
        form = ContactForm(initial={
            'next': next_url
            })

    display_form_title = getattr(settings, 'CONTACTFORM_DISPLAY_FORM_TITLE', True)
    framework = getattr(settings, 'CONTACTFORM_FRONTEND_FRAMEWORK', None)

    return {'form': form,
            'display_form_title': display_form_title,
            'framework': framework}

