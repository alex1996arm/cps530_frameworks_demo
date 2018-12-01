from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse(render(request, 'home.html'))


def credit(request):
    return HttpResponse(render(request, 'credits.html'))


def result(request):
    return HttpResponse(render(request, 'result.html'))


def summary(request):
    return HttpResponse(render(request, 'summary.html'))


def install(request):
    return HttpResponse(render(request, 'install.html'))


def sitetuto(request):
    return HttpResponse(render(request, 'sitetuto.html'))


def conclusion(request):
    return HttpResponse(render(request, 'conclusion.html'))

