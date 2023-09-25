from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404, HttpResponseRedirect

# Create your views here.
my_dict = {
    'sports': 'Sports Page',
    'finance' : 'Finance Page',
    'science': 'Science Page',
    'politics' : 'Politics Page',
    'military': 'Military Page'
}

def news_page(request, topic):
    try:
        result = my_dict[topic]
        return HttpResponse(my_dict[topic])
    except:
        result = 'Page not found'
        # return HttpResponseNotFound(result)
        raise Http404(result)
    

# we want to redirect the user from domain/third_app/0 --> domain/third_app/sports and so on

def redirect_user(request, number_of_the_page):
    topics_list = list(my_dict.keys())
    topic = topics_list[number_of_the_page] # we assume here that the user will provide us with a valid index that exists in the list

    return HttpResponseRedirect(topic)