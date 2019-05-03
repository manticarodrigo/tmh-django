from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from tmh.channels_app.consumers import ChatConsumer

websockets = URLRouter([
    path(
        'ws/chat/',
        ChatConsumer,
        name='ws_chat',
    ),
])

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(websockets),
})