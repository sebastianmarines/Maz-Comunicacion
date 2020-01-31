from django.urls import path, include

from . import views

app_name = "web"

urlpatterns = [
    path('', views.index),
    path('servicios/<slug:slug>/', include([
        path('', views.servicio, name="servicios"),
        path('<slug:subslug>', views.subservicio, name="servicio")
    ])),
]
