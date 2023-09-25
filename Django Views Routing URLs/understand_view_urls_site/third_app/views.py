from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404

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