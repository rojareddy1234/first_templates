from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def koushik(request):
    return HttpResponse('<marquee><h1> he is good boy he dont like go to school </marquee><h1>')
def school(request):
    return HttpResponse('<i>he is not going to school daily</i>')
