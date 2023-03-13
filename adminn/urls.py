from django.urls import path
from adminn import views
urlpatterns = [
    path('consulta-empresa',views.consultaEmpresa,name='consultaempresa'),
    path('registro-empresa',views.createEmpersa,name='createempresa'),
    path ('consulta-trabajadores', views.consultaTrabajador, name='consultatrabajador'),
    path('create-trabajador',views.createTrabajador,name='createtrabajador'),
    path('registro-solicitud',views.registroSolicitud,name='registrosolicitud'),
]