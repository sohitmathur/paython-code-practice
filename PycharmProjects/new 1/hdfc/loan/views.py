from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
# def home(r):
#     return HttpResponse('hi,from django server')
#
# def cricket(r):
#     return HttpResponse('boys played really well')
def personal_loan(r):
    return HttpResponse('<h1> hello , Response from the server</h1>')