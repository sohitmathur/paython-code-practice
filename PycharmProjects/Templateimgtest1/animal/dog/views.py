from django.shortcuts import render

# Create your views here.
def animal_cyl(r):
    animal_info = {'specie':'wild_animal','type':'raccoon','identy_no':125456}
    return render(r,'animal/specise.html',context=animal_info)

# Create your views here.
