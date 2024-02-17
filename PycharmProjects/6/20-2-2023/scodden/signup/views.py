from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def SignUpView(r):
    form=SignUpForm()



    return render(r,'signup/signup.html',{'form':form})