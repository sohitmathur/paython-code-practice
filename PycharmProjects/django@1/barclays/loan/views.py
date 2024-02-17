from django.shortcuts import render

# Create your views here.
def loan_info(r):
    return render(r,'loan/loan.html')
