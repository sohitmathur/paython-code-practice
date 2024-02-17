from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(r):
#     return HttpResponse('<h1>hi,from django server</h1>')

def scodden(r):
    my_dict={'name':'gajanan','city':'pune','fees':25000}
    return render(r,'loan/text.html',context=my_dict)

def wish(r):
    return render(r,'testapp/text.html',context={"abc":1234})