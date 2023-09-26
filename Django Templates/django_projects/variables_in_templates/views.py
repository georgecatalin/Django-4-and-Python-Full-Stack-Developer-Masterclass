from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound


# Create your views here.
def variable_view(request):

    my_variable_is_a_dictionary = {'first_name': 'George', 'last_name': 'Calin',
                                   'my_list': [1953, 1954, 1978], 'my_dictionary' : {'inside_key' : 'inside_value'}
                                   }

    return render(request, 'variables_in_templates/variables.html', context=my_variable_is_a_dictionary)


def example_view(request):
    return render(request, 'variables_in_templates/example.html')