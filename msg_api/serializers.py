from rest_framework import serializers
from msg_api import models

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Create_message
        fields = '__all__'
