from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohli(request):
    return HttpResponse('<h1>no1 batsman in the world</h1>')
def abd(request):
    return HttpResponse('<h1>MR.360</h1>')