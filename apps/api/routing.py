from django.urls import re_path
from .consumer import UpdatesConsumer

websocket_urlpatterns = [
    re_path(r"^ws/updates$", UpdatesConsumer.as_asgi()),
]