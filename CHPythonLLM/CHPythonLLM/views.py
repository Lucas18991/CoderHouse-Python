from multiprocessing import context
from re import template
from django.http import HttpResponse
import datetime
from django.template import Context, Template
import django
import socket


def saludo(request):
    return HttpResponse("Hola Mundo")


def segunda_vista(request):
    return HttpResponse("Esto es facil")


def dia_de_hoy(request):
    dia = datetime.datetime.today()
    cadena = "Hoy es " + str(dia)
    return HttpResponse(cadena)


def saludo_con_nombre(request, nombre):
    return HttpResponse("<h1> Hola mi nombre es: " + nombre + "<h1>")


def ano_nacimiento(request, edad):
    nacimiento = 2022 - int(edad)
    return HttpResponse("<h1> Hola ano nacimiento es: " + str(nacimiento) + "<h1>")


def probando_html(request):
    mihtml = open(
        "C:/Users/lucas/OneDrive/Documentos/CoderHouse-Python/CHPythonLLM/plantillas/template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    contexto = Context()
    documnto = plantilla.render(contexto)
    return HttpResponse(documnto)
