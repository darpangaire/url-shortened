from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Channels,ChannelsMemberShip
from django.contrib.auth import get_user_model

user = get_user_model()

class ChannelSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length = 255,required=True,validators = [UniqueValidator(queryset=Channels.objects.all())])
  description = serializers.CharField()
  
  class Meta:
    model = Channels
    fields = ["id","name","description","created_at"]
    read_only_fields = ["id","created_at"] # Auto-managed field
    
  def create(self, validated_data):
    request = self.context.get('request')
    user = request.user if request else None
    name = validated_data['name']
    description = validated_data['description']
    channels = Channels.objects.create(
      name=name,
      description=description,
      admin=user
    )
    return channels
  
class ChannelMembershipSerializer(serializers.ModelSerializer):
  class Meta:
    model = ChannelsMemberShip
    fields = ["id","channel"]
    
  def validate_channel(self,value):
    request = self.context.get('request')
    user = request.user if request else None
    
    if ChannelsMemberShip.objects.filter(channel = value,member = user).exists():
      raise serializers.ValidationError("you are already a member of this channel.")
    
    return value
  
    
  def create(self, validated_data):
    request = self.context.get('request')
    user = request.user if request else None
    channel = validated_data['channel']
    
    channelMembership = ChannelsMemberShip.objects.create(
      channel = channel,
      member = user
    )
    return channelMembership
    
