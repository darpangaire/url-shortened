from django.shortcuts import render,get_object_or_404
from .serializers import ChannelSerializer,ChannelMembershipSerializer,PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Channels,ChannelsMemberShip
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.

class ChannelCreateAPIView(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = ChannelSerializer
  
  def perform_create(self, serializer):
    serializer.save()
    
class ChannelMemberShipCreateAPIView(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = ChannelMembershipSerializer
  
  def perform_create(self, serializer):
    serializer.save()
    
class PostCreateAPIView(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = PostSerializer
  def perform_create(self, serializer):
    serializer.save()
    




# class ChannelViewSet(APIView):
#   permission_classes = [IsAuthenticated]
#   def post(self,request,format=None):
#     serializers = ChannelSerializer(data = request.data ,context={'request': request})
#     if serializers.is_valid():
#       serializers.save()
#       return Response({"success":"Successfully created channels..."},status=status.HTTP_201_CREATED)
#     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
#   # def update(self,request,format=None):
#   #   pass
  
#   def delete(self,request,format=None):
#     name = request.data.get('name')
#     if not name:
#       return Response({"error":"oops! channels name not found"},status=status.HTTP_400_BAD_REQUEST)
    
#     channel = get_object_or_404(Channels,name=name,created_by = request.user)
#     channel.delete()
#     return Response({"success":f"Channel {name} deleted successfully"},status=status.HTTP_204_NO_CONTENT)
  
  
  
#   def all_member(self,request,format=None):
#     name = request.data.get('name')
#     try:
#       channel = Channels.objects.get(name=name)
#     except:
#       return Response({"errors":"channels name does found"},status=status.HTTP_400_BAD_REQUEST)
    
#     members = channel.members.all()
#     return Response({"members":members},status=status.HTTP_200_OK)
        


#   def delete_members(self,request,format=None):
#     channel_name = request.data.get('name')
#     member_id = request.data.get('member')
#     if not channel_name and member_id:
#       return Response({"error":"channel name and members is does not found"},status=status.HTTP_400_BAD_REQUEST)
    
#     try:
#       channel = Channels.objects.get(name=channel_name,admin = request.user)
      
#     except Channels.DoesNotExist:
#       return Response({"error":"Channel not found or unauthorized."},status=status.HTTP_400_BAD_REQUEST)
    
#     try:
#       membership = ChannelsMemberShip.objects.get(channel=channel,member__id = member_id)
#       membership.delete()
#       return Response({"success":"successfully delete the member of that chanel"},status=status.HTTP_200_OK)
    
#     except ChannelsMemberShip.DoesNotExist:
#       return Response({"error":"Member not found in this channel"},status=status.HTTP_400_BAD_REQUEST)
    

#   def delete_post(self,request,format=None):
#     pass
    

  
  
    
    

 