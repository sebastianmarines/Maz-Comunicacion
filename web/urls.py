from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('servicios/<slug:slug>/', views.servicio),
]
