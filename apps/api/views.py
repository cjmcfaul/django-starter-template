from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from apps.users.models import (
    User,
)

from .serializers.users.user import (
    UserSerializer,
)


class UserDetail(APIView):

    def get_object(self, request, user_uuid):
        user = get_object_or_404(User, uuid=user_uuid)
        return user

    def get(self, request, user_uuid, format=None):
        user = self.get_object(user_uuid)
        serializer = UserSerializer(
            instance=user,
            request_user=request.user,
        )
        return Response(serializer.data)

    def put(self, request, user_uuid, format=None):
        user = self.get_object(user_uuid)
        serializer = UserSerializer(
            data=request.data,
            instance=user,
            request_user=request.user,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_uuid, format=None):
        user = self.get_object(user_uuid)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

