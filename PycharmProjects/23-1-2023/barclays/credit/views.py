from django.shortcuts import render

# Create your views here.
def credit_info(r):
    return render(r,'credit/credit_card_info.html')
