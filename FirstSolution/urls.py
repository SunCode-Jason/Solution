from django.urls import path
from FirstSolution import views

urlpatterns= [
    path('', views.login),
    path('login',views.login),
    path('index',views.index),
    path('homes',views.homes)
]
