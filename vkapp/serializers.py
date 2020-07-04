# -*- coding: utf-8 -*-
from vkapp.models import VKMessage, VKMessageGroup
from rest_framework import serializers

class VKMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VKMessage
        fields = ('userid', 'f_name', 'l_name', 'is_read', 'image_url', 'title', 'date', 'body', 'idmes')

class VKMesGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VKMessageGroup
        fields = ('userid', 'f_name', 'l_name', 'is_read', 'image_url', 'title', 'date', 'body', 'idmes')