from django.urls import path, include

from . import views

app_name = "periodicos"

urlpatterns = [
    path('portadas-y-columnas/', include([
        path('', views.portadas_list, name="portadas"),
        path('mexico/', views.portadas_list_mexico, name="portadas_mexico"),
        path('mexico/<slug:slug>/', views.portada_mexico, name="portada_mexico"),
        path('<slug:slug>/', views.portada, name="portada"),
    ]))
]