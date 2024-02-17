from django.shortcuts import render
from.forms import StudentRegistration


# Create your views here.
def costumor(r):
    return render(r,'life/life.html')

def showformdata(r):
    fm=StudentRegistration()
    return render(r,'life/userregistration.html',{'form':fm})

