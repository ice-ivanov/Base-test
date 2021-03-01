import json
from re import sub

from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self, *args, **kwargs):
        print('CONNECTED')
        print(self)
        print(type(self))
        print(self.__dict__)

        user_id = sub("[^0-9]", "", self.scope["path"])
        self.user = User.objects.get(pk=user_id)

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print('RECEIVE')
        print(self.user)

        print(self.user.__dict__)

        text_data_json = json.loads(text_data)
        if 'subject' in text_data_json:
            subject = text_data_json['subject']
            self._create_message(subject, self.user)
        else:
            self.send(text_data=json.dumps({'ERROR': 'Please select a subject'}))

        self.send(text_data=json.dumps({
            'text_data': text_data_json
        }))
