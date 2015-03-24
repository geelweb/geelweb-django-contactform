# -*- coding: utf-8 -*-

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


class ContactTestCase(TestCase):
    def test_form_displayed(self):
        """ Tests than the contact.html template is displayed
        """
        resp = self.client.get(reverse('contact'))
        self.assertContains(resp, 'Send us a message', status_code=200)

    def test_form_validation(self):
        """ Tests than the error messages are displayed
        """
        resp = self.client.post(reverse('contact'), {
            'subject': '',
            'message': '',
            'sender': '',
            'cc_myself': ''})
        self.assertContains(resp, 'This field is required.', status_code=200)

    def test_mail_sent(self):
        """ Tests than the email is sent
        """
        resp = self.client.post(reverse('contact'), {
            'subject': 'Plop !',
            'message': 'This is my message content',
            'sender': 'me@example.com'})

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'Plop !')

    def test_thanks_page_displayed(self):
        """ Tests than the thanks.html template is displayed
        """
        resp = self.client.post(reverse('contact'), {
            'subject': 'Plop !',
            'message': 'This is my message content',
            'sender': 'me@example.com'})
        self.assertContains(resp, 'Thanks for your message', status_code=200)
