from django.urls import path
from . import views


#URLCONF

urlpatterns = [
    path('', views.home),
    path('hello/', views.foua),
    path('helloworld/', views.test)
]