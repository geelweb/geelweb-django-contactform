from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^contact/$', 'geelweb.django.contactform.views.contact', name='contact'),
)

