from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # Import from chat/routing.py

# Define the protocol type router, integrating WebSocket routes
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)  # Use the WebSocket URL patterns defined in chat/routing.py
    ),
})
