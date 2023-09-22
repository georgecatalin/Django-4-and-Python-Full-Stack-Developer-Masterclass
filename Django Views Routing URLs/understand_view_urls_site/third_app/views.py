from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
my_dict = {
    'sports': 'Sports Page',
    'finance' : 'Finance Page',
    'science': 'Science Page',
    'politics' : 'Politics Page',
    'military': 'Military Page'
}

def news_page(request, topic):
    return HttpResponse(my_dict[topic])