from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def wish(r):
    return render(r,'testapp/abc.html',context={"abc":1234})
