from django.shortcuts import render
from . models import MobileModel
from . forms import MobileForm
from django.http import HttpResponseRedirect
def show_mobiles(r):
    stud_list = MobileModel.objects.all()

    my_dict = {'stud_list': stud_list}

    return render(r,'electronics/showmobiles.html',context=my_dict)

# Create your views here.
def mobile_view(r):
    form = MobileForm
    if r.method=='POST':
        form = MobileForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/showmobile')


    return render(r,'electronics/mobileinfo.html',{'form':form})
