from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'core/index.html')

def login (request):
    return render(request,'core/login.html')

def producto (request):
    return render(request,'core/producto.html')

def registro (request):
    return render(request,'core/registro.html')

def tienda (request):
    return render(request,'core/tienda.html')

def carrito (request):
    return render(request,'core/Carrito.html')

