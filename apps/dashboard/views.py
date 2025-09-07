from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request, "paginas/home.html")

def contato(request):

    return render(request, "paginas/contato.html")

def realtime(request):
    contexto = {
        "color": "text-red-500",
        "nome": "Eriton",
        "idade": 31,
        "lista": ["Python", "Django", "Jinja"],
    }
    return render(request, "paginas/real_time.html", contexto)

def htmx(request):

    now = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(fr"<p>Olá, mundo com HTMX! {now}</p>")

def tabela(request):
    return render(request, "paginas/tabela.html")