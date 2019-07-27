from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json

from tmh.core.models.user import User
from tmh.core.models.project import Project
from tmh.core.models.message import ProjectMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.commands[data['command']](self, data)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))

    async def fetch_messages(self, data):
        messages = await self.get_messages()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        await self.send(text_data=json.dumps(content))

    async def new_message(self, data):
        author = data['from']
        text = data['text']
        user = await self.get_user(author)
        project = await self.get_project(self.room_name)
        message = await self.create_message(user, project, text)
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        await self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': str(message.id),
            'author': message.author.get_short_name(),
            'content': message.content,
            'created_at': str(message.created_at)
        }

    async def send_chat_message(self, message):
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    @database_sync_to_async
    def get_messages(self):
        return ProjectMessage.objects.filter(project__pk=self.room_name)
    
    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)
    
    @database_sync_to_async
    def get_project(self, pk):
        return Project.objects.get(pk=pk)
    
    @database_sync_to_async
    def create_message(self, user, project, content):
        return ProjectMessage.objects.create(author=user, project=project, content=content)