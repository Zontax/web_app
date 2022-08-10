"""main APP URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tiles/', views.tiles, name='tiles'),
    path('randomint/', views.randomint, name='random'),
    path('about/', views.about, name='about'),
]
