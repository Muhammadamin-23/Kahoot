from django.urls import path
import consumers

websocket_urlpatterns = [
    path('ws/kahoot/<str:game_pin>/', consumers.KahootConsumer.as_asgi)
]
