from django.urls import path
from trabajador import views
urlpatterns = [
    path('create',views.create,name='createtrabajdor'),
    path ('consulta', views.consulta, name='consultatrabajador'),
    path ('editar', views.create, name='editartrabajador'),
    path ('eliminar', views.create, name='eliminartrabajador')
]