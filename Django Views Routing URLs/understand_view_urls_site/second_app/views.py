from django.shortcuts import render
from django.http import HttpResponse

my_dict = {
    'science': 'Science Page',
    'politics': 'Politics Page',
    'military': 'Military Page'
}

# Create your views here.
def sports_view(request):
    return HttpResponse("Sports Page")

def finance_view(request):
    return HttpResponse("Finance Page")

def science_view(request):
    return HttpResponse(my_dict['science'])

def politics_view(request):
    return HttpResponse(my_dict['politics'])

def military_view(request):
    return HttpResponse(my_dict['military'])