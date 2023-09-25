from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound

# Create your views here.

def simple_view(request):
    # first_app/templates/first_app/example.html
    return render(request,'first_app/example.html')