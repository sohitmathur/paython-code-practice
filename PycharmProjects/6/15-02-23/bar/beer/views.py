from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shop(r):
    my_dict = {'brand':'kingfisher','price':1000}
    return render(r,'beer/water.html', context=my_dict)
