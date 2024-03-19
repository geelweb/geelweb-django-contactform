from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
import requests

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        recaptcha_enabled = getattr(settings, 'GOOGLE_RECAPTCHA_ENABLED', False)
        recaptcha_valid = True
        if recaptcha_enabled:
            secret_key = settings.GOOGLE_RECAPTCHA_SECRET
            data = {
                'response': request.POST.get('g-recaptcha-response'),
                'secret': secret_key
            }
            resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result_json = resp.json()
            recaptcha_valid = result_json.get('success')

        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        comment = form.cleaned_data['comment']
        next = form.cleaned_data['next']

        site = get_current_site(request)

        tpl = getattr(settings, 'CONTACTFORM_MSG_TEMPLATE', 'contactform/message.txt'),
        message = render_to_string(tpl, {
            'site': site,
            'email': email,
            'phone': phone,
            'comment': comment})

        if recaptcha_valid:
            recipients = settings.CONTACTFORM_RECIPIENTS
            try:
                email = EmailMessage(
                        getattr(settings, 'CONTACTFORM_SUBJECT', _('New message')),
                        message,
                        getattr(settings, 'CONTACTFORM_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL),
                        recipients,
                        reply_to=[email])
                email.send(fail_silently=False)
            except BadHeaderError:
                 return HttpResponse('Invalid header found.')


        messages.success(request, _('Your message has been sent.'), extra_tags='contactform')

        if next != '':
            return redirect(next)

        use_thanks_page = getattr(settings, 'CONTACTFORM_USE_THANKS_PAGE', True)
        if use_thanks_page:
            return render(request, 'contactform/thanks.html')

    return render(request, 'contactform/contact.html', {
        'form': form})
