from django.urls import path
from trabajador import views
urlpatterns = [
    path('editar-perfil/',views.editarPerfil,name='editarperfil'),
    path('inicio',views.inicio,name='iniciotrabajdor'),
    path ('editar/<int:editar>', views.editar, name='editartrabajador'),
    path ('eliminar/<int:eliminacion>', views.eliminar, name='eliminartrabajador'),
    path('credencial/', views.credencial, name='credencial'),
    path('remision/', views.remision, name='remision'),
    path('pago-mensual/', views.pago, name='pago'),
]