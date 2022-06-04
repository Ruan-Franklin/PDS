#Para acessar a view do GameProfile, é necessário esse arquivo .py
from django.urls import path
from . import views
urlpatterns =[
  path('', views.index, name='index'),
  ]
