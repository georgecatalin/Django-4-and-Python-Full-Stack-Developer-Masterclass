from django.shortcuts import render, redirect
from . import models
from django.urls import reverse

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    my_context_dictionary = { 'all_cars_key': all_cars}


    return render(request, 'cars/list.html', context= my_context_dictionary)


def add(request):
    print(request.POST) # e.g. -> <QueryDict: {'csrfmiddlewaretoken': ['n9E2sEjoZRZNehLTQZUi50MgnpXCvCSaUMEwxBNHpzvz89Eg13zH6PwAxz7n1nHB'], 'brand': ['Renault'], 'year': ['2007']}>
    if request.POST:
        brand_value = request.POST['brand']
        year_value = int(request.POST['year'])
        models.Car.objects.create(brand=brand_value, year= year_value)
        
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        print(request.POST)
        primary_key = request.POST['record_id']
        
        try:
            models.Car.objects.get(pk=primary_key).delete()
            return redirect(reverse('cars:list'))
        except:
            print('There is not such primary key in the database')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')