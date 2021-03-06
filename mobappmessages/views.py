from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mobappmessages.models import ModAppMess
from mobappmessages.serializers import MobAppMessSerializer


@api_view(['GET', 'POST'])
def mobappmess(request):
    if request.method == 'GET':
        messages = ModAppMess.objects.all()
        serializer = MobAppMessSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MobAppMessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)