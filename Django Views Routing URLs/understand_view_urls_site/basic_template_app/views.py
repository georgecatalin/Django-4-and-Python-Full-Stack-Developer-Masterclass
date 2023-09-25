from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse


# Create your views here.
def simple_view(request):
    return render(request, 'basic_template_app/example.html')

