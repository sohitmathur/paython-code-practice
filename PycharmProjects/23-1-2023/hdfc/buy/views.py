from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loan_ac(r):
    return HttpResponse('<h1> loan start from the loan_ac</h1>')
def credit_cc(r):
    return HttpResponse('<h1> credit start from the loan_ac</h1>')
def buy_dc(r):
    return HttpResponse('<h1> buy start from the loan_ac</h1>')

