from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello from main view")  # later on we can connect to templates for HTML from here, and use JINJA to fill in the templates