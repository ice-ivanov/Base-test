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
from django.contrib.postgres.aggregates.general import ArrayAgg

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
        print(self.user.roles.all())

        all_roles = list(UserRole.objects.all())
        user_roles = list(self.user.roles.all())
        # TODO: Make a proper query
        manager = all_roles[0]
        student = all_roles[1]
        # user_roles
        if student in user_roles:
            # print(message)
            self._manager_notify(message, subject)

    def _manager_notify(self, message, subject):
        subject_obj = Subject.objects.get(name=subject)
        users = User.objects.all()
        manager_obj = UserRole.objects.get(name='manager')

        print('MESSAGE')
        print(message)
        print(type(message))

        print(self.channel_layer.channels)
        print(type(self.channel_layer.channels))

        self.send(text_data=json.dumps({
            'message': message
        }))

        # async_to_sync(self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }))

        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'from': self.user.username,
        #         'message': message
        #     }
        # )

        print('SENT')

        for user in users:
            if subject_obj in user.subjects.all() and manager_obj in user.roles.all():
                print('FIRST IF')
                print(f'chat_{user.id}')
                # print(self.channel_layer.groups[f'chat_{user.id}'])
                if f'chat_{user.id}' in self.channel_layer.groups:
                    print('it is here')
                    for group in self.channel_layer.groups:
                        print(group)
                        # self.chat_message(group, message)

                        # async_to_sync(self.channel_layer.group_send)(
                        #     group,
                        #     {
                        #         'type': 'chat_message',
                        #         # 'from': user.username,
                        #         'message': 'message'
                        #     }
                        # )

            # if subject.name in user.subjects.all():
            #     print('Huzza!')

            #     print(user)
        # print(subject_obj[0].pizzas.all()
        # managers = User.objects

    # Receive message from room group
    # def chat_message(self, group):
    #     print('SEND!')
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': self.message
    #         }
    #     )
