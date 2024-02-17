from django.shortcuts import render
from .form import ShirtModel

# Create your views here.
def shirt(r):
    obj=ShirtModel()
    return render(r,'cloths/shirts.html',{"form":obj})
