from . import views
from django.urls import path

urlpatterns = [
    path('sports/', views.sports_view, name='sports'),
    path('finance/', views.finance_view, name='finance'),
    path('science/', views.science_view, name = 'science'),
    path('politics/', views.politics_view, name='politics')
]