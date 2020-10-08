from django.http import HttpResponse


def saludo(request):
    return HttpResponse("<h1>Hola Chus. Esta es la primera página con Django</h1>")


def despedida(request):
    return HttpResponse("<h1 style='color:blue;'> Hasta luego Chus</h1>")