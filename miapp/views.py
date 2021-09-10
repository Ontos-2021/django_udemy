from django.shortcuts import render, HttpResponse


# Create your views here.
# MVC = Modelo Vista Controlador (El controlador hace acciones)
# MVT = Modelo Templates Vistas -> La vista hace acciones (Métodos)

def index(request):
    return HttpResponse("""
        <h1>Inicio</h1>
    """)


def hola_mundo(request):
    return HttpResponse("""
    <h1>¡Hola Mundo con Django!</h1>
    <p>Esta es mi primera vista con Django</p>
    """)


def pagina(request):
    return HttpResponse("""
    <h1>Página de mi web</h1>
    <p>Creado por Ontos</p>
    """)
