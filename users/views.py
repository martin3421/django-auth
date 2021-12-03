from django.shortcuts import render
from rest_framework import generics
from .models import NewUser
from .serializers import UserSerializer

# Create your views here.

class UserDetail(generics.RetrieveAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
