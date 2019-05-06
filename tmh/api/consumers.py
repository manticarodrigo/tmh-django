from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from tmh.core.models.user import User
from tmh.core.models.project import Project
from tmh.core.models.message import ProjectMessage

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave group room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))

    ###
    ## Commands
    ###

    def init_chat(self, data):
        username = data['username']
        user = User.objects.get(username=username)
        content = {
            'command': 'init_chat'
        }
        if not user:
            content['error'] = 'Unable to get user with username: ' + username
            self.send(text_data=json.dumps(content))
        content['success'] = 'Chatting in ' + self.room_name + ' with success with username: ' + username
        self.send(text_data=json.dumps(content))

    def fetch_messages(self, data):
        messages = ProjectMessage.objects.filter(project__pk=self.room_name)
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send(text_data=json.dumps(content))

    def new_message(self, data):
        author = data['from']
        text = data['text']
        user = User.objects.get(username=author)
        project = Project.objects.get(pk=self.room_name)
        message = ProjectMessage.objects.create(author=user, project=project, content=text)
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': str(message.id),
            'author': message.author.username,
            'content': message.content,
            'created_at': str(message.created_at)
        }

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    commands = {
        'init_chat': init_chat,
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }