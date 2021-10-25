from django import http
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle

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
        <a href="/hola_mundo-django">Hola Mundo</a>
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
    """
    html = ""
        <h1>Inicio</h1>
        <p>Números del 1 al 100</p>
        <ul>
    ""
    numero = 1
    while numero <= 100:
        html += f"<li>{str(numero)}</li>"
        numero += 1

    html += "</ul>"

    """

    year = 2021
    hasta = range(year, 2051)

    nombre = "José Mercado"
    lenguajes = ["JavaScript", "Python", "PHP", "C"]

    return render(request, "index.html", {
        "title": "Inicio",
        "mi_variable": "Soy un dato que está en la vista",
        "nombre": nombre,
        "lenguajes": lenguajes,
        "years": hasta
    })


def hola_mundo(request):
    return render(request, "hola_mundo.html")


def pagina(request, redirigir=0):
    if redirigir == 1:
        # return redirect("/contacto/José/Mercado")
        return redirect("contacto", nombre="José", apellido="Mercado")

    return render(request, "pagina.html", {
        "texto": "Este es mi texto",
        "lista": ["Uno", "Dos", "Tres"]
    })


def contacto(request, nombre="", apellido=""):
    html = ""
    if nombre and apellido:
        html += """
            <p>el nombre completo es:</p> 
            """
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout + "<h2>Contacto</h2>" + html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )

    articulo.save()

    return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")


def save_article(request):
    if request.method == 'POST':

        title = request.POST["title"]
        print(title)

        if len(title) <= 1:
            return HttpResponse("<h1>El título es muy pequeño</h1>")

        content = request.POST["content"]
        public = request.POST["public"]

        articulo = Article(
            title=title,
            content=content,
            public=public
        )

        articulo.save()
        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")


def create_article(request):
    return render(request, "create_article.html")


def create_full_article(request):
    if request.method == "POST":

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get("title")
            content = data_form["content"]
            public = data_form["public"]

            articulo = Article(
                title=title,
                content=content,
                public=public
            )

            articulo.save()

            return redirect("articulos")
            # return HttpResponse(articulo.title + " - " + articulo.content + " - " + str(articulo.public))

    else:

        formulario = FormArticle()

    return render(request, "create_full_article.html", {
        "form": formulario
    })


def articulo(request):
    try:
        articulo = Article.objects.get(title="Segundo Artículo", public=True)
        response = f"Artículo: {articulo.id}. </br>{articulo.title}"
    except:
        response = "<h1>Artículo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Superman"
    articulo.content = "Película de un chabón que vuela"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Artículo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")


def articulos(request):
    """articulos = Article.objects.filter(title__iexact="Artículo")
    Contains | Si lo contiene o no (Ignora mayúsculas)
    iexact | Es si coincide ignorando mayúsculas
    filter.gt (greater than) .lt (less than) .lte (less than or equal)
    filtar.gte (greater than or equal)
    return HttpResponse(articulos)

    articulos = Article.objects.filter(
        title__iexact = "Artículo pulento"
    ).exclude(public=True)"""

    articulos = Article.objects.raw(
        "SELECT id, title from miapp_article WHERE title='Artículo' AND public=1"
    )

    articulos = Article.objects.filter(
        Q(title__contains="Artículo") | Q(title__contains="Pulento")
    )

    articulos = Article.objects.all().order_by("-id")

    return render(request, "articulos.html", {
        "articulos": articulos
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect("articulos")
