from django.shortcuts import render

# Create your views here.
def credit_info(r):
    return render(r,'credit/creditcardinfo.html')