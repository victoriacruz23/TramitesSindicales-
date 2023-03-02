from django.urls import path
from adminn import views
urlpatterns = [
    path('registro-empresa',views.createEmpersa,name='createempresa'),
]