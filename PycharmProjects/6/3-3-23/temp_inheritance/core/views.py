from django.shortcuts import render

# Create your views here.
def home(r):
    return render(r,'core/home.html')

def about(r):
    return render(r,'core/about.html')
