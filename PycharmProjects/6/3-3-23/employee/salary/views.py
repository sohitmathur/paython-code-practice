from django.shortcuts import render
from datetime import datetime
# Create your views here.
def total_sal(r):

    # emp= 'sohit'
    # emp_dept= 'devloper'
    # emp_sal= 100000
    # my_dict={'nm':emp,'fu':emp_dept,'su':emp_sal}

     d= datetime.now()
     # return render(r, 'salary/salary.html',{'dt':d})
     # return render(r, 'salary/salary.html',{'gm':'sohit','st':5})
     # student={'names':['sohit','rohit','mohit','arjun','akash']}
     data = {'stu1': {'name':'sohit','sal':100000,'designation':'data scientist'},
              'stu2':{'name':'sohit','sal':100000,'designation':'data scientist'},}

     return render(r,'salary/salary.html',{'data':data})