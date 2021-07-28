from django.shortcuts import render, HttpResponse

# Create your views here.
def hello (request, name, idade):
    return HttpResponse(f"<h1>Hello {name} de {idade} anos! Venha brincar comigo!</h1>")

def soma(request, n1, n2):
    return HttpResponse(f"<h1>Somando: {n1} + {n2} = {n1+n2}</h1>")

def subtr(request, n1, n2):
    return HttpResponse("<h1>Subtraindo: {} - {} = {}</h1>".format(n1, n2, (n1 - n2)))

def multipl(request, n1, n2):
    return HttpResponse("<h1>Multiplicando: {} x {} = {}</h1>".format(n1, n2, (n1 * n2)))

def divs(request, n1, n2):
    return HttpResponse("<h1>Dividindo: {} / {} = {}</h1>".format(n1, n2, (n1 / n2)))