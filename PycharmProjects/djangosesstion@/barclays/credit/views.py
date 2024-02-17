from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def credit_info(r):
    print("sbc")
    template = loader.get_template('creditcardinfo.html')
    return HttpResponse(template.render())
