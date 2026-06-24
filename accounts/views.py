from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Views in Django are more like request and actions

def home(request):
    return HttpResponse('Good morning Django !')

def foua(request):
    return HttpResponse('Hello world')


def test(request):
    return render(request, 'hello.html', {'name': 'Zack Efron'})