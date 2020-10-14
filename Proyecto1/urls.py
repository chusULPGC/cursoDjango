"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),    
    path('fecha/', dame_Fecha),
    path('edades/<int:edad>/<int:agno>',calcula_Edad), #recibe como parametro la edad y el año(hay que convertirlo a int)
    path('cursoc/', cursoC),
    path('cursodjango/', cursoDjango),


]
