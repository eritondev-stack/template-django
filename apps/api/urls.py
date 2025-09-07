from django.urls import path, re_path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="api-ping"),
    path("atualiza/", views.api_atualiza, name="api_atualiza"),
    path("clientes", views.clientes, name="api_clientes")
]