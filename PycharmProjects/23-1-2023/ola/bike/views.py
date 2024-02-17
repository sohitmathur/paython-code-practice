from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bike_cc(r):
    return HttpResponse('<h1> from bike server</h1>')
def car_cc(r):
    return HttpResponse('<h1> from car server</h1>')
def auto_kick(r):
    return HttpResponse('<h1> from auto server</h1>')
