from django.urls import path
from sesion import views
"""importacion de la app"""
"""direccionamiento de los html"""
urlpatterns = [
    path('registro/', views.hola,name='registro'),
    path('cerrar/', views.cerrar_sesion, name='cerrada'),

]
