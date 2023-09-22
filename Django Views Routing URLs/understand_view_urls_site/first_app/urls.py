from django.urls import path
from . import views

urlpatterns =[ 
    path('', views.simple_view, name='simple_view'),
    path('<int:number1>/<int:number2>', views.add_view,name="add_numbers")
    ]