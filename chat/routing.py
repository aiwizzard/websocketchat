from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/group_chat_main/', consumers.ChatConsumer.as_asgi())
]