from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gopika(request):
    return HttpResponse('<h1> gopika is became a good dancer</h1>')
def dance(request):
    return HttpResponse('<b> she likes dancing very much</b>')