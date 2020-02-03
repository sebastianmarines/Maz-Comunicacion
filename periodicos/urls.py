from django.urls import path, include

from . import views

app_name = "periodicos"

urlpatterns = [
    path('portadas-y-columnas/', include([
        path('coahuila/', views.portadas_list, name="portadas"),
        path('coahuila/<slug:slug>/', views.portada, name="portada"),
        path('mexico/', views.portadas_list_mexico, name="portadas_mexico"),
        path('mexico/<slug:slug>/', views.portada_mexico, name="portada_mexico"),
        path('nuevo-leon/', views.portadas_list_nl, name="portadas_nl"),
        path('nuevo-leon/<slug:slug>', views.portada_nl, name="portada_nl"),
    ]))
]