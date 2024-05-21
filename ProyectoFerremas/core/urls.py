from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('producto', producto, name="producto"),
    path('registro', registro, name="registro"),
    path('tienda', tienda, name="tienda"),
    path('carrito', carrito, name="carrito"),
    path('metodosPago', metodosPago,name="metodosPago"),
    path('transferencia', transferencia,name="transferencia")
]
