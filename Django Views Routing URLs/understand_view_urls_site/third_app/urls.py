from . import views
from django.urls import path

urlpatterns = [
    path('<int:number_of_the_page>', views.redirect_user),
    path('<str:topic>/', views.news_page, name='topic-page')
]