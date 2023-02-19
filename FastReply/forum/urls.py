from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('devs/', views.devs, name='devs'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login, name='login'),
]
