from django.urls import path
from . import views

app_name = "apps.dashboard"
urlpatterns = [
    path("", views.home, name="home"),             
    path("contato/", views.contato, name="contato"),
    path("real-time/", views.realtime, name="real-time"),
    path("htmx/", views.htmx, name="htmx"),
    path("tabela/", views.tabela, name="tabela"),
]