from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import (RegistrationSerializer,)
from rest_framework.decorators import api_view
from .models import User
from drf_yasg.utils import swagger_auto_schema


class RegistrationAPIView(CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Overide the default post()
        """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return_message = {"message": "Registration successful"}
        serializer.save()
        return Response(return_message, status=status.HTTP_201_CREATED)
