import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from custom_auth.models import UserRole
from django.contrib.auth import get_user_model
from chat.models import Subject

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        kwargs = self.scope["url_route"]['kwargs']
        user_id = kwargs['user_id']
        self.user = User.objects.get(pk=user_id)

        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = str(user_id)
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        print('HEHEHE')
        print(self.room_group_name)
        print(self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        subject = text_data_json['subject']

        self._select_user_type(message, subject)

    def _select_user_type(self, message, subject):
        # Send message to room group
        print('Now select users to send to!')
        print(self.channel_layer.__dict__)
        print(self.__dict__)
        print(self.user.role.all())
        all_roles = list(UserRole.objects.all())
        user_roles = list(self.user.role.all())
        # TODO: Make a proper query
        manager = all_roles[0]
        user = all_roles[1]
        if user in user_roles:
            print('User asking question!')
            self._manager_notify(subject)
        # if

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def _manager_notify(self, subject):
        subject_obj = Subject.objects.filter(name=subject)
        print(subject_obj)
        # managers = User.objects

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
