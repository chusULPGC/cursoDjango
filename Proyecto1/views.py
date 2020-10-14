from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template #para cargar plantillas
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido






def saludo(request):

    p1=Persona("Rut","Barrero")

    nombre="Chus"
    apellido="Izquierdo Puebla"

    ahora=fecha_actual=datetime.datetime.now()

    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    return render(request,"plantillaSaludo.html",{"nombre_persona":nombre, "apellido_persona":apellido,
                                                  "ahora":ahora,"name":p1.nombre,"apellido":p1.apellido,
                                                  "temas":temasDelCurso})


def despedida(request):
    documento="""<html>
                <head>
                </head>
                <body>
                <h1 style='color:blue;'> Hasta luego Chus</h1>
                </body>
                </html>"""
    return HttpResponse(documento)



def dame_Fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
                <head>
                </head>
                <body>
                <h1>
                Fecha y hora actuales %s
                </h1>
                </body>
                </html>"""% fecha_actual

    return HttpResponse(documento)


def calcula_Edad(request, edad, agno):    #pasamos como parametro la edad y el año
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="""<html>
                <body>
                <h1>
                En el año %s tendras %s años
                </h1>
                </body>
                </html>""" %(agno, edadFutura)
    return HttpResponse(documento)


def cursoC(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "cursoC.html",{"dameFecha":fecha_actual})


    
def cursoDjango(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "cursoDjango.html",{"dameFecha":fecha_actual})