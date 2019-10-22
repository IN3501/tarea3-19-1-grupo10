from django.urls import path
from .views import *

urlpatterns = [
    path('', homeCliente, name='homeCliente'),
    path('inputs/', inputs, name='inputs'),
    path('contacto', contacto, name='contacto'),
    path('agenda', agenda, name='agenda'),
    path('catalogo', catalogo, name='catalogo'),
    path('agendaReg', agendaReg, name = 'agendaReg'),
    path('contacto_exitoso', contacto_exitoso, name = 'contacto_exitoso'),

    path('backoffice', backoffice, name='backoffice'),
    path('homeEmpresa', homeEmpresa, name='homeEmpresa'),
    path('fichaClinica', fichaClinica, name='fichaClinica'),
    path('resumen_fichaClinica', resumen, name='resumen_fichaClinica'),
    path('estadisticas', estadisticas, name='estadisticas'),
    path('inventario', inventario, name='inventario'),
    path('comprar', comprarObjeto, name='comprarObjeto'),
    path('agregarElemento', agregarElemento, name='agregarElemento'),
    path('envioInventario',envioInventario, name='envioInventario'),

    path('registrar_usuario', registrar_usuario, name='registrar_usuario'),
    path('mostrar_resultado', recuperar_registro, name='mostrar_resultado'),
    path('add_pet', add_pet, name='add_peth'),
    path('client_profile', client_profile, name='client_profile'),
    path('login', login, name='login'),

    path('payment', payment, name='payment'),
    path('shopping-cart', shopping_cart, name='shopping_cart')
]
