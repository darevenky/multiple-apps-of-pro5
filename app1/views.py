from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first_app1(request):
    return HttpResponse('first of app1')

def second_app1(request):
    return HttpResponse('second of app1')