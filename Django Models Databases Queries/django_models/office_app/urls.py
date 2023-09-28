from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_records, name='list_records')
]
