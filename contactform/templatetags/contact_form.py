from django import template
from django.conf import settings

from contactform.forms import ContactForm

register = template.Library()

@register.simple_tag(takes_context=True)
def contact_form(context, form=None):
    if form is None:
        form = ContactForm()

    template_name = 'contactform/form.html'
    framework = getattr(settings, 'CONTACTFORM_FRONTEND_FRAMEWORK', None)
    if framework == 'bootstrap':
        template_name = 'contactform/form_bootstrap.html'

    if framework == 'uikit':
        template_name = 'contactform/form_uikit.html'

    t = context.template.engine.get_template(template_name)
    return t.render(template.RequestContext(context.request, {'form': form}, autoescape=context.autoescape))

