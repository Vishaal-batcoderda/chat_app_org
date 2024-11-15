import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP request routing
    "websocket": AuthMiddlewareStack(  # WebSocket routing
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
