from django.urls import path
from ProyectoPag import views

urlpatterns = [

    path('tienda', views.tienda, name="Tienda"),
    path('inicio', views.inicio, name="Inicio"),
    path('servicio', views.servicio, name="Servicio"),
    path('contacto', views.contacto, name="Contacto"),
]