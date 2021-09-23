from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista Controlador (El controlador hace acciones)
# MVT = Modelo Templates Vistas -> La vista hace acciones (Métodos)

layout = """
    
    <h1>Sitio web con Django | Ontos</h1>
    <hr/>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola_mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Números del 1 al 100</p>
        <ul>
    """
    numero = 1
    while numero <= 100:
        html += f"<li>{str(numero)}</li>"
        numero += 1

    html += "</ul>"
    return render(request, "index.html")


def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir=0):

    if redirigir == 1:
        ##return redirect("/contacto/José/Mercado")
        return redirect("contacto", nombre="José", apellido="Mercado")

    return render(request, "pagina.html")


def contacto(request, nombre="", apellido=""):
    html = ""
    if nombre and apellido:
        html += """
            <p>el nombre completo es:</p> 
            """
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout + "<h2>Contacto</h2>" + html)
