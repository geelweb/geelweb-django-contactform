from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

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


@register.simple_tag()
def contact_form_btn(label, form_id):
    btn_attrs = {'class': ''}

    framework = getattr(settings, 'CONTACTFORM_FRONTEND_FRAMEWORK', None)
    if framework == 'uikit':
        btn_attrs['class'] = 'uk-button uk-button-primary'
    elif framework == 'bootstrap':
        btn_attrs['class'] = 'btn btn-primary'

    recaptcha_enabled = getattr(settings, 'GOOGLE_RECAPTCHA_ENABLED', False)
    if recaptcha_enabled:
        btn_attrs['class'] += ' g-recaptcha'
        btn_attrs['data-sitekey'] = getattr(settings, 'GOOGLE_RECAPTCHA_SITE_KEY', '')
        btn_attrs['data-callback'] = 'onDjangoContactFormSubmit'
        btn_attrs['data-action'] = 'submit'
    else:
        btn_attrs['type'] = 'submit'

    btn = """<button %s>%s</button>""" % (
        ' '.join(['%s="%s"' % (k, btn_attrs[k].strip()) for k in btn_attrs if btn_attrs[k] != '']),
        label)

    if recaptcha_enabled:
        btn += '\n<script>function onDjangoContactFormSubmit(token) { document.getElementById("%s").submit(); }</script>' % form_id

    return mark_safe(btn)
