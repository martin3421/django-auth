from rest_framework import serializers
from .models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'user_name']