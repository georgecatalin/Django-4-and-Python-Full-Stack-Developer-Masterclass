from django.shortcuts import render
from . import models

# Create your views here.
def list_records(request):

    all_records = models.Patient.objects.all()

    my_context_dictionary = {'patients' : all_records}

    return render(request, 'office_app/list.html',context=my_context_dictionary )
