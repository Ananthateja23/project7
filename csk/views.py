from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jadeja(request):
    return HttpResponse('<h1>Good all rounder</h1>')
def raina(request):
    return HttpResponse('<h1>Best friend to dhoni</h1>')