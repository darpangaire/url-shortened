from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Channels,ChannelsMemberShip,Post,PostImages
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

user = get_user_model()

class ChannelSerializer(serializers.ModelSerializer):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  name = serializers.CharField(max_length = 255,required=True,validators = [UniqueValidator(queryset=Channels.objects.all())])
  description = serializers.CharField()
  image = serializers.ImageField(required=False, allow_null=True)
  
  class Meta:
    model = Channels
    fields = ["id","name","description","created_at","image"]
    read_only_fields = ["id","created_at"] # Auto-managed field
    
  def create(self, validated_data):
    request = self.context.get('request')
    user = request.user if request else None
    name = validated_data['name']
    description = validated_data['description']
    image = validated_data.get('image','None')
    channels = Channels.objects.create(
      name=name,
      description=description,
      image = image,
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
 
 
class PostImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostImages
    fields = ["id","images"]
  


   
class PostSerializer(serializers.ModelSerializer):
  images = PostImageSerializer(many=True,write_only = True,required = False)
  title = serializers.CharField(max_length = 255,required = True)
  description = serializers.CharField()
  class Meta:
    model = Post
    fields = ["id","title","description","channel","images"]
    
  def validate_channel(self,value):
    request = self.context.get('request')
    user = request.user if request else None
    
    if not user or not user.is_authenticated:
      raise serializers.ValidationError("Authentication required.")
    
    if not ChannelsMemberShip.objects.filter(channel = value,member = user).exists():
      raise serializers.ValidationError("you are not a member of this channel.")
    
    return value
  
  def create(self, validated_data):
    images_data = validated_data.pop('images', [])
    post = super().create(validated_data)
    for image_data in images_data:
        PostImages.objects.create(post=post, images=image_data['images'])
    return post
  
  

 
