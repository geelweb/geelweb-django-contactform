from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
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

        recipients = settings.CONTACTFORM_RECIPIENTS
        try:
            send_mail(
                    getattr(settings, 'CONTACTFORM_SUBJECT', _('New message')),
                    message,
                    email,
                    recipients,
                    fail_silently=False)
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
