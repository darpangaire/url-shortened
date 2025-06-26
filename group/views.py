from django.shortcuts import render,get_object_or_404
from .serializers import ChannelSerializer,ChannelMembershipSerializer,PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Channels,ChannelsMemberShip
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth.decorators import login_required
from .models import Channels

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
  parser_classes = (MultiPartParser, FormParser)
  def get_serializer_context(self):
    context = super().get_serializer_context()
    context['request'] = self.request
    return context
  
  
 
def home(request):
  channels = Channels.objects.all()
  context = {
    "channels":channels
  }
  return render(request,'index.html',context)



def channels(request):
  return render(request,'channels.html')

@login_required(login_url='login')  
def create_channels(request):
  return render(request,'create_channels.html')


def channel_details(request,id):
  channel = get_object_or_404(Channels,id=id)
  posts = channel.posts.prefetch_related('images').order_by('-created_at')
  context = {
    'channel': channel,
    'posts': posts,
  }
  print("Request User:", request.user)
  print("Channel Admin:", channel.admin)
  return render(request,'channel_details.html',context)


  
  

  
  
    
    

 