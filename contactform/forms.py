from django import forms
from django.utils.translation import ugettext as _

class ContactForm(forms.Form):
    email = forms.EmailField(
                label=_('Email'),
                widget=forms.TextInput(
                    attrs={
                        'placeholder': _('Your email address')
                        }
                    )
                )
    phone = forms.CharField(
                label=_('Phone'),
                widget=forms.TextInput(
                    attrs={
                        'placeholder': _('+33...')
                        }
                    )
                )
    comment = forms.CharField(
                label=_('Comment'),
                widget=forms.Textarea(
                    attrs={
                        'placeholder': _('Your message'),
                        'rows': 8,
                        'cols': 80
                        }
                    )
                )

    next = forms.CharField(required=False, widget=forms.HiddenInput())

