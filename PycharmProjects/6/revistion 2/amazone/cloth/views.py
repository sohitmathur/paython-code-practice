from django.shortcuts import render
from django.shortcuts import StudentForm
# from testapp.forms import StudentForm

def student_input_view(request):
 sent=False
 if request.method=='POST':
  form=StudentForm(request.POST)
 if form.is_valid():
  print('Form Validation Success and printing data')
  print('Name:',form.cleaned_data['name'])
  print('Marks:',form.cleaned_data['marks'])
  sent=True
 form=StudentForm()
 return render(request,'cloth/shirt.html',{'form':form,'sent':sent})