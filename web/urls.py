from django.urls import path, include

from . import views

app_name = "web"

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/<slug:slug>/', include([
        path('', views.servicio, name="servicios"),
        path('<slug:subslug>/', views.subservicio, name="servicio")
    ])),
    path('contacto/', views.contact, name="contacto"),
    path('politica-de-privacidad/', views.politica_privacidad, name="privacy-policy"),
    path('politica-de-cookies/', views.politica_cookies, name="cookie-policy")
]
