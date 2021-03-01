import json
from django.shortcuts import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from custom_auth.models import UserRole
from channels.auth import channel_session_user_from_http
from channels import Group

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('CONNECTED')
        print(self.__dict__)

        kwargs = self.scope["url_route"]['kwargs']
        user_id = kwargs['user_id']
        self.user = User.objects.get(pk=user_id)

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print('RECEIVE')
        print(self.user)

        user_roles = self.user.role.through.objects.filter(user_id=self.user)
        roles = list()
        for role in user_roles:
            role_name = UserRole.objects.get(id=role.id)
            roles.append(role_name)

        self._send_to_subject(roles)

        'New stuff'
        text_data_json = json.loads(text_data)
        if 'subject' in text_data_json:
            subject = text_data_json['subject']
            self._create_message(subject, self.user)
        else:
            self.send(text_data=json.dumps({'ERROR': 'Please select a subject'}))

        self.send(text_data=json.dumps({
            'text_data': text_data_json
        }))

    def _send_to_subject(self, roles):
        print(roles)
        print(self.__dict__)
        self.send(text_data=json.dumps({
            'text_data': str(self.__dict__)
        }))

    # def alarm(self):
    #     layer = get_channel_layer()
    #     async_to_sync(layer.group_send)('events', {
    #         'type': 'events.alarm',
    #         'content': 'triggered'
    #     })

    # @channel_session_user_from_http
    # def ws_connect(self, message):
    #     Group("user-{}".format(self.user.id)).add(message.reply_channel)
