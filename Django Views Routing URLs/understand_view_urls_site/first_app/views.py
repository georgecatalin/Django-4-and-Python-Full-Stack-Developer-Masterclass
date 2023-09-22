from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse("Hello from first_app/")

def add_view(request, number1, number2):
    ''' we  want to pass ../first_app/num1/num2  and get the result in the page '''
    add_result = number1 + number2
    result = "{0} + {1} = {2}".format(number1,number2,add_result)
    return HttpResponse(str(result))