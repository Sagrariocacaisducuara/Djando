from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render



class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre

        self.apellido=apellido


def saludo(request):
    p1=Persona("profesor juan","Diaz")
    # nombre = "juan"
    # apellido = "Diaz"
    temasDelCurso = ["plantillas","modelos","formularios","vistas","Despliegue"]
    ahora = datetime.datetime.now()
    # doc_externo = open("C:/xampp/htdocs/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    #doc_externo=get_template('miplantilla.html')
    #ctx = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" :ahora, "temas":temasDelCurso})
    #documento = doc_externo.render({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" :ahora, "temas":temasDelCurso})
    return render(request, "miplantilla.html",{"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" :ahora, "temas":temasDelCurso})

def curso(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"CursoC.html",{"dameFecha":fecha_actual})
def cursoCSS(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"cursoCSS.html",{"dameFecha":fecha_actual})



def despedida(request):
    return HttpResponse("Hasta luego")


def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = f"<html><body><h1>Fecha y hora actuales {fecha_actual}</h1></body></html>"
    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual = 18
    periodo = agno - 2023
    edadFutura = edadActual + periodo
    documento = f"<html><body><h2>En el año {agno} tendrás {edadFutura} años</h2></body></html>"
    return HttpResponse(documento)


# def calculaEdad(request,edad, agno):

#     #edadActual=18
#     periodo=agno-2023
#     edadFutura=edad+periodo
#     documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

#     return HttpResponse(documento)