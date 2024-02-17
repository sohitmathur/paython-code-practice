from django.shortcuts import render

# Create your views here.
def courseinfo(r):
    return render(r,'course/courseinfo.html')
