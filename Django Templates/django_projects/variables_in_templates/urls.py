from . import views
from django.urls import path, include

#register the application namespace to be used with the URL Names
app_name = 'variables_in_templates'

urlpatterns = [
    path('variables/', views.variable_view, name='variable'),
    path('', views.example_view, name='example')

]