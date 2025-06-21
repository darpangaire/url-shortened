from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Channels
from django.contrib.auth import get_user_model

user = get_user_model()

class ChannelSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length = 255,required=True,validators = [UniqueValidator(queryset=Channels.objects.all())])
  description = serializers.CharField()
  
  class Meta:
    model = Channels
    fields = ["name","description"]
    
  def create(self, validated_data):
    request = self.context.get('request')
    user = request.user if request else None
    name = validated_data['name']
    description = validated_data['description']
    channels = Channels.objects.create(
      name=name,
      description=description,
      created_by=user
    )
    return channels
  


