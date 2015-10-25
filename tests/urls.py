from django.conf.urls import url
from geelweb.django.contactform import views

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
]

