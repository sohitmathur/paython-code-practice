from django.shortcuts import render
from.models import BookDemoModel
from.forms import BookDemoForm
from django.http import HttpResponseRedirect

# Create your views here.
def BookDemoView(r):
    form = BookDemoForm()
    if r.method =='POST':
        form= BookDemoForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')




    return render(r,'bookdemo/demo.html',{'form':form})

