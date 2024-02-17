from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def auto_index(r):
    return HttpResponse('<h1> auto from ola</h1>')
