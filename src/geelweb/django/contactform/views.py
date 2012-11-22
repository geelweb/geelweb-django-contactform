from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from geelweb.django.contactform.models import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = settings.CONTACTFORM_RECIPIENTS
            if cc_myself:
                recipients.append(sender)

            send_mail(getattr(settings, "CONTACTFORM_SUBJECT_PREFIX", '') + subject, message, sender, recipients)

            return render_to_response(
                'contactform/thanks.html',
                {},
                context_instance=RequestContext(request))
    else:
        form = ContactForm()

    return render_to_response(
            'contactform/contact.html',
            {'form': form},
            context_instance=RequestContext(request))

