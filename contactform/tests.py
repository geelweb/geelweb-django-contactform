from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

class ContactTestCase(TestCase):
    def test_form_displayed(self):
        """ Tests than the contact.html template is displayed
        """
        resp = self.client.get(reverse('contactform:index'))
        self.assertContains(resp, 'csrfmiddlewaretoken', status_code=200)
        self.assertContains(resp, 'Contact us', status_code=200)

        with self.settings(CONTACTFORM_FRONTEND_FRAMEWORK='uikit'):
            resp = self.client.get(reverse('contactform:index'))
            self.assertContains(resp, 'csrfmiddlewaretoken', status_code=200)
            self.assertContains(resp, 'Contact us', status_code=200)
            self.assertContains(resp, 'uk-input')

        with self.settings(CONTACTFORM_FRONTEND_FRAMEWORK='bootstrap'):
            resp = self.client.get(reverse('contactform:index'))
            self.assertContains(resp, 'csrfmiddlewaretoken', status_code=200)
            self.assertContains(resp, 'Contact us', status_code=200)
            self.assertContains(resp, 'form-control')

    def test_form_validation(self):
        """ Tests than the error messages are displayed
        """
        resp = self.client.post(reverse('contactform:index'), {
            'email': '',
            'phone': '',
            'comment': ''})
        self.assertContains(resp, 'This field is required.', status_code=200)

    @override_settings(CONTACTFORM_RECIPIENTS=['contact@example.com'])
    def test_mail_sent(self):
        """ Tests than the email is sent
        """
        resp = self.client.post(reverse('contactform:index'), {
            'email': 'me@example.com',
            'phone': '06 00 00 00 00',
            'comment': 'This is my message content'})

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'New message')
        self.assertIn('06 00 00 00 00', mail.outbox[0].body)
        self.assertIn('This is my message content', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].from_email, 'me@example.com')
        self.assertEqual(mail.outbox[0].to, ['contact@example.com'])

        self.assertContains(resp, 'Thanks for your message', status_code=200)

        with self.settings(CONTACTFORM_SUBJECT='My custom subject'):
            resp = self.client.post(reverse('contactform:index'), {
                'email': 'me@example.com',
                'phone': '06 00 00 00 00',
                'comment': 'This is my message content'})
            self.assertEqual(mail.outbox[1].subject, 'My custom subject')

    def test_next_param(self):
        resp = self.client.post(reverse('contactform:index'), {
            'email': 'me@example.com',
            'phone': '06 00 00 00 00',
            'comment': 'This is my message content',
            'next': '/'}, follow=True)

        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirects(resp, '/')
