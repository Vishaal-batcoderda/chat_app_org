import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # Import routing from the chat app

# Ensure DJANGO_SETTINGS_MODULE is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP request routing
    "websocket": AuthMiddlewareStack(  # WebSocket routing
        URLRouter(
            websocket_urlpatterns  # Use the WebSocket URL patterns defined in chat/routing.py
        )
    ),
})
