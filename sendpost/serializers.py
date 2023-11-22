from rest_framework import serializers
from .models import Client, Mailing, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class MailingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mailing
        fields = ['url', 'pk', 'id', 'start_time', 'end_time', 'message_text']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer()
    mailing = MailingSerializer()

    class Meta:
        model = Message
        fields = ['url', 'pk', 'id', 'created_at', 'status', 'client', 'mailing']