from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(render(request, 'home.html'))


def credit(request):
    return HttpResponse(render(request, 'credits.html'))

def result(request):
    return HttpResponse(render(request, 'result.html'))
