from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(r):
    return render(r, 'emp_app/index.html')


def all_emp(r):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)

    return render(r, 'emp_app/view_all_emp.html', context)


def add_emp(r):
    if r.method == 'POST':
        first_name = r.POST['first_name']
        last_name = r.POST['last_name']
        salary = int(r.POST['salary'])
        bonus = int(r.POST['bonus'])
        role = int(r.POST['role'])
        phone = int(r.POST['phone'])
        dept = int(r.POST['dept'])
        # hire_date=int(r.post['datetime.now'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, dept_id=dept, bonus=bonus,
                           phone=phone, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')

    elif r.method == 'GET':
        return render(r, 'emp_app/add_emp.html')
    else:
        return render('an Exception Occured! Employee has not been Added!')


def remove_emp(r, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully')

        except:
            HttpResponse('please enter valid employee id')
    emps = Employee.objects.all()
    context = {
        'emps': emps

    }

    return render(r, 'emp_app/remove_emp.html', context)


def filter_emp(r):
    if r.method == 'POST':
        name = r.POST['name']
        dept = r.POST['dept']
        role = r.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__contains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
           'emps': emps
        }

        return render(r, 'emp_app/view_all_emp.html', context)

    elif r.method == 'GET':
        return render(r,'emp_app/filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')



