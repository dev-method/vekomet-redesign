from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vekomet_redesign import settings
from rest_framework import status
from vkapp.models import VKMessage, VKMessageGroup
from vkapp.serializers import VKMesSerializer, VKMesGroupSerializer
# Create your views here.

@login_required(login_url='/admin/')
def vk_messages(request):
    return render(request, 'vkapp/{}/vk_messages.html'.format(settings.TEMP_PREFIX))

@api_view(['GET'])
def mes_collection(request):
    if request.method == 'GET':
        messages = VKMessage.objects.all()
        serializer = VKMesSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def mes_element(request, idmes):
    try:
        message = VKMessage.objects.get(idmes=idmes)
    except VKMessage.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = VKMesSerializer(message)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def mes_group_collection(request):
    if request.method == 'GET':
        messages = VKMessageGroup.objects.all()
        serializer = VKMesGroupSerializer(messages, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def mes_group_element(request, idmes):
    try:
        message = VKMessageGroup.objects.get(idmes=idmes)
    except VKMessageGroup.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = VKMesGroupSerializer(message)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)