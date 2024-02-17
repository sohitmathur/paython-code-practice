from django.http import HttpResponse
from django.shortcuts import render

def chrome(r):
    return render(r,'google/index.html')
def display(r):
    return HttpResponse('Hii! this is sohit')
def show(r):
    return HttpResponse(r'<h1> hello this is google </h1>')
def course_detail(r,courseid):
    return HttpResponse(courseid)