from django import template
from django.conf import settings

from contactform.forms import ContactForm

register = template.Library()

@register.simple_tag(takes_context=True)
def contact_form(context, form=None, *args, **kwargs):
    if form is None:
        next_url = kwargs['next'] if 'next' in kwargs else None
        form = ContactForm(initial={
            'next': next_url
            })

    display_form_title = getattr(settings, 'CONTACTFORM_DISPLAY_FORM_TITLE', True)

    template_name = 'contactform/form.html'
    framework = getattr(settings, 'CONTACTFORM_FRONTEND_FRAMEWORK', None)
    if framework == 'bootstrap':
        template_name = 'contactform/form_bootstrap.html'

    if framework == 'uikit':
        template_name = 'contactform/form_uikit.html'

    t = context.template.engine.get_template(template_name)
    return t.render(template.RequestContext(context.request, {
        'form': form,
        'display_form_title': display_form_title
        }, autoescape=context.autoescape))

