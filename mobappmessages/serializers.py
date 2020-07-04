from mobappmessages.models import ModAppMess
from rest_framework import serializers

class MobAppMessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModAppMess
        fields = ('name', 'phone','mail', 'message')

