from django.urls import path
from adminn import views
urlpatterns = [
    path('registro-empresa',views.createEmpersa,name='createempresa'),
    path('consulta-empresa',views.consultaEmpresa,name='consultaempresa'),
    path('registro-solicitud',views.registroSolicitud,name='registrosolicitud'),
]