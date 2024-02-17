from django.shortcuts import render
from.models import employee
from .forms import FeedbackForm

# Create your views here.
# def student(r):
#     stud_list=student.object.all
#     print(stud_list)
#     my_dict={'stud_list':stud_list}
#     return render(r,'credit/credit.html',context=my_dict)

# def feedback_show(r):
#     form = FeedbackForm()
#     my_dict = {'form':form}
#     return render(r,'credit/feedback.html',context=my_dict)

def feedback_show(r):
    form = FeedbackForm()
    if r.method=='POST':
        form = FeedbackForm(r.POST)
        if form. is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    return render(r,'credit/feedback.html',{'form':form})

