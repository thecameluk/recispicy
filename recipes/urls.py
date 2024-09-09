
from django.contrib import admin
from django.urls import path
from  recipes import views


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipes'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
