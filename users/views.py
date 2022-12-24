from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializer import RegistrationSerializer, UserSerializer


# Create your views here.

class RegisterApiView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def form(self, request):
        serializer = self.serializer_class(data=request.date)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetUserAPI(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)

