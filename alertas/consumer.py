import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class AlertaConsumer(WebsocketConsumer):
    
    async def connect(self):
        self.tipo = 'alerta_toast'
        self.tipoAlerta = self.tipo
        
        await self.channel_layer.group_add(
            self.tipoAlerta,
            self.channel_name
        )
        
        self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.tipoAlerta,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msj = text_data_json["msj"]
        
        await self.channel_layer.group_send(
            self.tipoAlerta,
            {
                'type': 'any',
                'msj': msj
            }
        )

        self.send(text_data=json.dumps({"msj": msj}))
        
    async def msjAlerta(self, event):
        msj = event['msj']
        
        await self.send(text_data=json.dumps({
            'msj': msj
        }))