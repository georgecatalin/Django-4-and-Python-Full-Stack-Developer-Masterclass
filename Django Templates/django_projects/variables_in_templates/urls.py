from . import views
from django.urls import path, include

urlpatterns = [
    path('variables/', views.variable_view)
]