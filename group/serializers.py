from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Channels,ChannelsMemberShip,Post
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
    
class PostSerializer(serializers.ModelSerializer):
  title = serializers.CharField(max_length = 255,required = True)
  description = serializers.CharField()
  class Meta:
    model = Post
    fields = ["id","title","description","channel"]
    
  def validate_channel(self,value):
    request = self.context.get('request')
    user = request.user if request else None
    
    if not user or not user.is_authenticated:
      raise serializers.ValidationError("Authentication required.")
    
    if not ChannelsMemberShip.objects.filter(channel = value,member = user).exists():
      raise serializers.ValidationError("you are not a member of this channel.")
    
    return value
  
  def create(self, validated_data):
    channel = validated_data.get('channel')
    if not channel:
      raise serializers.ValidationError({"channel": "Channel is required."})
    title = validated_data['title']
    description = validated_data['description']
    
    post = Post.objects.create(channel=channel,title=title,description=description)
    return post
  
  
 
