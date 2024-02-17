from django.shortcuts import render
import datetime



date_and_time = datetime.datetime.now()

def agri_info(r):
    date_and_time = datetime.datetime.now()
    my_dict = {'dateandtime':str(date_and_time)}
    # personal_details = {'name':'Sohit','salary':100000,'age':25}
    return render(r,'agri/agriinfo.html',context=my_dict)
def agri_product(r):
    return render(r,'agri/agriproduct.html')