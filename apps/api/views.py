# apps/api/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.timezone import now
import random, time
from faker import Faker
fake = Faker('pt_BR')

# Aqui você buscaria do banco
data = [
        {"id":"1001","cliente":"Ana Lima","status":2,"valor":1234.56,"dataEpoch":1735603200},
    ]
count = 0


def clientes(request):
    global data
    global count
    data.append({"id":count+1010,"cliente":fake.name(),"status":random.choice([1, 2, 3]),"valor":random.randint(100,2000),"dataEpoch":1704067200},)
    count += 1
    
    
    return JsonResponse({"data": data})

def ping(request):
    return JsonResponse({"ok": True})

@csrf_exempt  # para demo. Em produção, proteja com autenticação/CSRF/token.
def api_atualiza(request):
    """
    Exemplo de endpoint de API (POST/GET) que dispara push p/ todos conectados.
    """
    print("API /atualiza/ chamada")
    channel_layer = get_channel_layer()
    html = f"<div id='result2' hx-swap-oob='true'>Atualizado: {now()}</div>"

    # Envia ao grupo "updates" (todos navegadores conectados em /ws/updates)
    async_to_sync(channel_layer.group_send)(
        "updates",
        {"type": "broadcast_html", "html": html}
    )
    return JsonResponse({"ok": True})