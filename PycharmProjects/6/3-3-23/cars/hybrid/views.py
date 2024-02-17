from django.shortcuts import render,HttpResponse
from.models import Employee,Role,Department
from datetime import datetime

# Create your views here.
def index(r):
    return render(r,'hybrid/hybrid.html')


def all_emp(r):
    emps= Employee.objects.all()
    context={
        'emps':emps
    }

    print(context)
    return render(r, 'hybrid/all_emp.html',context)
def add_emp(r):
    if r.method == 'POST':
        first_name = r.POST['first_name']
        last_name = r.POST['last_name']
        salary = int(r.POST['salary'])
        bonus = int(r.POST['bonus'])
        dept = r.POST['dept']
        phone = int(r.POST['phone_no'])
        role = r.POST['role']
        hire_date = int(r.POST['hire_date'])
        new_emp =Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()

        return HttpResponse('Employee added successfully')
    elif r.method=='GET':
         return render(r,'hybrid/add_emp.html')
    else:
        return render('An Exception occured!Employee has not been added')



    return render(r,'hybrid/add_emp.html')
def remove_emp(r):
    return render(r,'hybrid/remove_emp.html')
def filter_emp(r):
    return render(r,'hybrid/filter_emp.html')