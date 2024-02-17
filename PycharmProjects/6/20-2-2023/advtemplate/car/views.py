from django.shortcuts import render

# Create your views here.
def car_info(r):
    return render(r,'car/carinfo.html')

def petrol(r):
    return render(r,'car/petroal.html')
def diesel(r):
    return render(r,'car/diesel.html')
def cng(r):
    return render(r,'car/cng.html')
def electrical(r):
    return render(r,'car/electrical.html')
