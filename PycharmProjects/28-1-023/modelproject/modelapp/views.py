from django.shortcuts import render
from. models import Student
from.forms import FeedbackForm

import pandas as pd

# Create your views here.
def show_student(r):
    stud_list = Student.objects.all()
    print(stud_list)
    my_dict = {'stud_list':stud_list}
    return render(r,'studentform.html',context=my_dict)

def feedback_show(r, form=None):
    form = FeedbackForm()
    my_dict = {'form':form}
    return render(r, 'modelapp/feedbackform.html',context=my_dict)

