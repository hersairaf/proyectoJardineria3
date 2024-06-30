from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('ClientesAdd/', views.ClientesAdd, name='ClientesAdd'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('clientes_findEdit/<str:pk>/', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientes_del/<str:pk>/', views.clientes_del, name='clientes_del'),
    path('ClientesUpdate/', views.ClientesUpdate, name='ClientesUpdate'),

]