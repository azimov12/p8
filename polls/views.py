from django.shortcuts import render
from django.http import HttpResponse

def function1(request):
    return HttpResponse('This is Function 1')

def function2(request):
    return HttpResponse('This is Function 2')