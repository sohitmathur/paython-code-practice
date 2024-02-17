from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,'home/index.html')
def logout(r):
    return render(r,'home/logout.html')