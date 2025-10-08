from django.contrib import admin
from django.urls import path

from instacaio import views

urlpatterns = [
    path('postar/', views.criar_post, name='postar'),
    path('', views.inicio, name='inicio'),
]
