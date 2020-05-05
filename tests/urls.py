from django.urls import include, path
from . import views

urlpatterns = [
     path('', views.index),
     path('custom/', views.custom),
     path('contact/', include('contactform.urls')),
]
