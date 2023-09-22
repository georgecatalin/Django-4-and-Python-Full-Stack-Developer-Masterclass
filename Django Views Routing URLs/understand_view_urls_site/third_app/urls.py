from . import views
from django.urls import path

urlpatterns = [
    path('<str:topic>/', views.news_page)
]