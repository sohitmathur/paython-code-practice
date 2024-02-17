from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bike_cc(r):
    return HttpResponse('<h1> bike_cc from ola server</h1>')
def car_ac(r):
    return HttpResponse('<h1> car_ac is on from server</h1>')
def auto_kick(r):
    return HttpResponse('<h1> auto_kick is on from server</h1>')
