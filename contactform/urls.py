from django.urls import path
from . import views

app_name = 'contactform'

urlpatterns = [
    path('', views.index, name='index')
]
