from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarse/', views.registrar_vuelo, name='registrar_vuelo'),
    path('lista/', views.listadevuelos, name='listadevuelos'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]