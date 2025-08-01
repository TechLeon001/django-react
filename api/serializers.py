from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class meta:
        model = User
        fields =["id","username","password"]
        extra_kwargs = {"password": {"write_only":True}}


  def create(self,validated_data):
      user = User.objects.create_user(**validated_data)
 
      return user
