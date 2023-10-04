from django.urls import path
from .views import (HomeView, ThankYouView, ContactFormView, 
                    TeacherCreateView, TeacherListView)

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'), # path expects a function
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list/', TeacherListView.as_view(), name='list')
]