from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first_app2(request):
    return HttpResponse('first of app2')

def second_app2(request):
    return HttpResponse('second of app2')