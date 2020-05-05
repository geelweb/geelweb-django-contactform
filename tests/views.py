from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Page content')

def custom(request):
    return render(request, 'custom.html', {})
