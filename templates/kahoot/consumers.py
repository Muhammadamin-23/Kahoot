import json

from channels.generic.websocket import AsyncWebsocketConsumer


class KahootConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.game_pin = self.scope['url_route']['kwargs']['game_pin']
        self.room_group_name = f'kahoot_{self.game_pin}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'player_join',
                "username": username
            }
        )
