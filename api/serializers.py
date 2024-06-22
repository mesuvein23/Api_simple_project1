# Serializers converts your complex data into python data
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    phone = serializers.IntegerField()
    email = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Contact.objects.create(** validated_data)

    def update(self,data, validated_data):
        newdata=Contact(**validated_data)
        newdata.id = data.id
        newdata.save()
        return newdata

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
  