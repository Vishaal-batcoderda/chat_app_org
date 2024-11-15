from django.urls import path
from .consumers import ChatConsumer

# Define WebSocket URL patterns for the chat app
websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),  # WebSocket route for the chat
]
