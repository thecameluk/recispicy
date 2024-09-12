
from django.contrib import admin
from django.urls import path
from  recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
