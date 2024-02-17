from django.shortcuts import render


# Create your views here.
def display(r):
    my_dict= {
        'title':'Zoom Car',
        'zoom':'Car Services',
        'cars':['suv','sidan','jeep'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'sohit','phone':7020294941},
            {'name':'tohit', 'phone':7020294945}

        ]


    }
    return render(r,'car/car.html',my_dict)