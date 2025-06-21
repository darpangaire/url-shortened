from django.shortcuts import render,get_object_or_404
from .serializers import ChannelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Channels
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ChannelViewSet(APIView):
  permission_classes = [IsAuthenticated]
  def post(self,request,format=None):
    serializers = ChannelSerializer(data = request.data ,context={'request': request})
    if serializers.is_valid():
      serializers.save()
      return Response({"success":"Successfully created channels..."},status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
  # def update(self,request,format=None):
  #   pass
  
  def delete(self,request,format=None):
    name = request.data.get('name')
    if not name:
      return Response({"error":"oops! channels name not found"},status=status.HTTP_400_BAD_REQUEST)
    
    channel = get_object_or_404(Channels,name=name,created_by = request.user)
    channel.delete()
    return Response({"success":f"Channel {name} deleted successfully"},status=status.HTTP_204_NO_CONTENT)
  
  
  def patch(self,request,format=None):
    pass
  
  
  
    
  
  
    