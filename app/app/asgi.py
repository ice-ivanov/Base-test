import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
from django.urls import re_path
from myapp import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"^front(end)/$", consumers.AsyncChatConsumer.as_asgi()),
        ])
    ),

})
