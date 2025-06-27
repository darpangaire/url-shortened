from django.shortcuts import render,get_object_or_404,redirect
from .serializers import ChannelSerializer,ChannelMembershipSerializer,PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Channels,ChannelsMemberShip
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib.auth.decorators import login_required
from .models import Channels,Post,PostImages,Comment
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from account.backends import get_user_from_jwt_for_backend
from account.utils import sending_email
from django.core.paginator import Paginator

# Create your views here.

User = get_user_model()

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
  paginator = Paginator(channels,4)
  page = request.GET.get('page')
  paged_channels = paginator.get_page(page)
  channel_count = channels.count()
  
  
  context = {
    "channels":paged_channels,
    "channel_count":channel_count
  }
  return render(request,'index.html',context)


def channels(request):
  return render(request,'channels.html')

 
def create_channels(request):
  user = get_user_from_jwt_for_backend(request)
  if user:
    return render(request,'create_channels.html')
  
  else:
    return redirect('login')
  


  
  
def channel_details(request,id):
  channel = get_object_or_404(Channels,id=id)
  user = get_user_from_jwt_for_backend(request)
  posts = channel.posts.prefetch_related('images').order_by('-created_at')
  context = {
    'channel': channel,
    'posts': posts,
    


  }
  print(user)

  return render(request,'channel_details.html',context)

def create_Post(request,id):
  if request.method == 'POST':
    channel = get_object_or_404(Channels,id=id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    post = Post.objects.create(
      channel=channel,
      title = title,
      description = description
    )
    
    for image in request.FILES.getlist('images'):
      PostImages.objects.create(post=post,images = image)
      
    return redirect('channel_details',id=id)
  
def delete_post(request,id):
  post = get_object_or_404(Post,id=id)
  user = get_user_from_jwt_for_backend(request)
  if user != post.channel.admin:
    return HttpResponseForbidden("You are not allowed to delete this post.")
  
  PostImages.objects.filter(post=post).delete()
  post.delete()
  return redirect('channel_details',id=post.channel.id)   
  

def create_comment(request,id):
  if request.method == "POST":
    post = get_object_or_404(Post,id=id)
    name = request.POST.get('name')
    textArea = request.POST.get('text')
    
    Comment.objects.create(post=post,name=name,text = textArea)
    sending_email(request,post)
    return redirect('channel_details',id=post.channel.id) 
  

def delete_comment(request,id):
  if request.method == 'POST':
    comment = get_object_or_404(Comment,id=id)
    user = get_user_from_jwt_for_backend(request)
    if user == comment.post.channel.admin:
      comment.delete()
    else:
      return HttpResponseForbidden("you cannot delete comment only admin can.")
    return redirect('channel_details',id=comment.post.channel.id)
    

  

 