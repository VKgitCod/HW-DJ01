from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Домашняя работа на Django</h1>")

def data(request):
    return HttpResponse("<h1>Страница DATA из ДЗ</h1>")

def test(request):
    return HttpResponse("<h1>Страница TEST из ДЗ</h1>")