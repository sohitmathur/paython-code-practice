from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(r):
    context ={

        'variable1':'this is my dictionery' ,
        'variable2':'this is my dictionery2'
    }
    return render(r,'home/index.html',context)

def about(r):
    return render(r,'about.html')
    # return HttpResponse('<h1> hii  this is about page</h1')


def services(r):
    return render(r,'services.html')
    # return HttpResponse('<h1> hii  this is services page</h1')

def contact(r):
    return render(r,'contact.html')
    # return HttpResponse('<h1> hii  this is contact page</h1')