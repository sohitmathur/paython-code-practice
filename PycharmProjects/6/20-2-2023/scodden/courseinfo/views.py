from django.shortcuts import render
from.models import CourseInfoModel,StudRegistration
from .forms import StudRegForm,CourseInfoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def CourseInfoView(r):
    stud_list = CourseInfoModel.objects.all()


    return render(r,'courseinfo/course_info.html',{'stud_list':stud_list})


def PythonRegView(r):
    form = StudRegForm()
    if r.method == 'POST':
        form = StudRegForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(r, 'courseinfo/python.html', {'form': form})
@login_required
def PythonInfoView(r):
    stud_list = StudRegistration.objects.all()
    return render(r,'courseinfo/pythonlist.html',{'stud_list':stud_list})
@login_required
def Course_Update(r,id):
    obj = CourseInfoModel.objects.get(id=id)
    if  r.method=='POST':
        form = CourseInfoForm(r.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courseinfo/course/')

    return render(r,'courseinfo/update.html',{'obj': obj})

def delete(r,id):
    obj = CourseInfoModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/courseinfo/course/')
