from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
'''
def home_view(request):
    return render(request, 'classroom/home.html') # this is the old way through a function based view
'''

class HomeView(TemplateView):
    template_name = 'classroom/home.html' # Through the attribute connect it to forms or models

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # it will look for model_form.html
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you') # reverse() use in function & reverse_lazy() use in class. reverse() returns a string & reverse_lazy() returns an object

class TeacherListView(ListView):
    model = Teacher
    # it is looking for the template model_list.html
    queryset = Teacher.objects.all()    # here is the query to apply on the records
    context_object_name = 'teacher_list'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html' # reverse_lazy('classroom:thank_you')

    #  where to go if successful
    success_url = '/classroom/thank_you/' # Add a forward slash to make it an absolute URL

    # what to do with the form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)