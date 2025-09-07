from channels.generic.websocket import AsyncWebsocketConsumer

class UpdatesConsumer(AsyncWebsocketConsumer):
    group_name = "updates"

    async def connect(self):
        # entra no grupo "updates" (broadcast)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Método chamado via group_send(type="broadcast_html", ...)
    async def broadcast_html(self, event):
        html = event["html"]
        # Envie HTML com hx-swap-oob='true' p/ atualizar qualquer alvo por id
        await self.send(text_data=html)
