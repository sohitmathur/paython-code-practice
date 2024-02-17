from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saving_acc(r):
    return HttpResponse('<h1> from saving account</h1>')
def current_acc(r):
    return HttpResponse('<h1> from current account</h1>')
def cash_cc(r):
    return HttpResponse('<h1> from cash cc account</h1>')
