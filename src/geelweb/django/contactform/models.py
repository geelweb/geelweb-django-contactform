#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""Django contactform models"""

from django import forms
from django.utils.translation import ugettext as _

class ContactForm(forms.Form):
    """Contact form"""
    subject = forms.CharField(label=_('Subject'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)
    sender = forms.EmailField(label=_('Sender email'))
    cc_myself = forms.BooleanField(label=_('Send me a copy'), required=False)

