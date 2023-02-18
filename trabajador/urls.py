from django.urls import path
from trabajador import views
urlpatterns = [
    path('create',views.create,name='createtrabajdor'),
    path ('consulta', views.consulta, name='consultatrabajador'),
    path ('editar/<int:editar>', views.editar, name='editartrabajador'),
    path ('eliminar/<int:eliminacion>', views.eliminar, name='eliminartrabajador')
]