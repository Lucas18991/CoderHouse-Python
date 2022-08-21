from multiprocessing import context
from re import template
from django.http import HttpResponse
import datetime
from django.template import Context, Template
import socket
from django.template import loader

nom = "carlos"
ape = "Basq"
datos = {"nombre": nom, "apellido": ape, "fecha": datetime.datetime.now()}


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

    plantilla = loader.get_template('template1.html')
    contexto = Context()
    documnto = plantilla.render(datos)
    return HttpResponse(documnto)
