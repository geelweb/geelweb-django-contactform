from django.core import mail
from django.template import Template, RequestContext
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from .forms import ContactForm

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
        self.assertIn('New message from testserver', mail.outbox[0].body)
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

        with self.settings(CONTACTFORM_USE_THANKS_PAGE=False):
            resp = self.client.post(reverse('contactform:index'), {
                'email': 'me@example.com',
                'phone': '06 00 00 00 00',
                'comment': 'This is my message content'})
            self.assertNotContains(resp, 'Thanks for your message', status_code=200)

    def test_next_param(self):
        resp = self.client.post(reverse('contactform:index'), {
            'email': 'me@example.com',
            'phone': '06 00 00 00 00',
            'comment': 'This is my message content',
            'next': '/'}, follow=True)

        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirects(resp, '/')

    def test_cutom_contact_page(self):
        resp = self.client.get('/custom/')
        self.assertInHTML('<input type="hidden" name="next" id="id_next" value="/custom/">', u"%s" % resp.content)

        resp = self.client.post(reverse('contactform:index'), {
            'email': 'me@example.com',
            'phone': '06 00 00 00 00',
            'comment': 'This is my message content',
            'next': '/custom/'}, follow=True)
        self.assertRedirects(resp, '/custom/')

        self.assertContains(resp, 'Your message has been sent.', status_code=200)
        self.assertInHTML('<input type="hidden" name="next" id="id_next" value="/custom/">', u"%s" % resp.content)

    @override_settings(CONTACTFORM_DISPLAY_FORM_TITLE=False)
    def test_form_title_not_displayed(self):
        resp = self.client.get(reverse('contactform:index'))
        self.assertContains(resp, 'csrfmiddlewaretoken', status_code=200)
        self.assertNotContains(resp, '<h3>Contact us</h3>', status_code=200)


class ContagFormTagTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_tag_without_param(self):
        tpl = Template("{% load contact_form %}{% contact_form %}")

        content = tpl.render(RequestContext(self.factory.get('/contact'), {}))
        self.assertInHTML('<input type="text" name="email" placeholder="Your email address" required id="id_email">', content)
        self.assertInHTML('<input type="text" name="phone" placeholder="+33..." required id="id_phone">', content)
        self.assertInHTML('<textarea name="comment" cols="80" rows="8" placeholder="Your message" required id="id_comment"></textarea>', content)
        self.assertInHTML('<input type="hidden" name="next" id="id_next">', content)

    def test_tag_with_form_param(self):
        tpl = Template("{% load contact_form %}{% contact_form form %}")

        form = ContactForm(initial={
            'email': 'me@example.com',
            'phone': '06 12 34 56 78',
            'comment': 'Plop',
            'next': '/'})

        content = tpl.render(RequestContext(self.factory.get('/contact'), {'form': form}))
        self.assertInHTML('<input type="text" name="email" placeholder="Your email address" required id="id_email" value="me@example.com">', content)
        self.assertInHTML('<input type="text" name="phone" placeholder="+33..." required id="id_phone" value="06 12 34 56 78">', content)
        self.assertInHTML('<textarea name="comment" cols="80" rows="8" placeholder="Your message" required id="id_comment">Plop</textarea>', content)
        self.assertInHTML('<input type="hidden" name="next" id="id_next" value="/">', content)

    def test_tag_with_next_arg(self):
        tpl = Template("""{% load contact_form %}{% contact_form next="/"%}""")

        content = tpl.render(RequestContext(self.factory.get('/contact'), {}))
        self.assertInHTML('<input type="text" name="email" placeholder="Your email address" required id="id_email">', content)
        self.assertInHTML('<input type="text" name="phone" placeholder="+33..." required id="id_phone">', content)
        self.assertInHTML('<textarea name="comment" cols="80" rows="8" placeholder="Your message" required id="id_comment"></textarea>', content)
        self.assertInHTML('<input type="hidden" name="next" id="id_next" value="/">', content)


