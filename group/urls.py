from django.urls import path
from .views import ChannelCreateAPIView,ChannelMemberShipCreateAPIView,PostCreateAPIView,home,channels,create_channels,channel_details,create_Post,delete_post,create_comment,delete_comment

urlpatterns = [
  path('api/create-channel/',ChannelCreateAPIView.as_view(),name='createchannel'),
  path('api/join-channels/',ChannelMemberShipCreateAPIView.as_view(),name='join-channels'),
  path('api/create-posts/',PostCreateAPIView.as_view(),name='create-posts'),
  
  path('',home,name='home'),
  path('channels/',channels,name='channels'),
  path('create-channels/',create_channels,name = "create-channels"),
  path('channels/<int:id>/', channel_details, name='channel_details'),
  path('create-post/<int:id>/', create_Post, name='create_Post'), 
  path('delete-post/<int:id>/', delete_post, name='delete_post'), 
  path('create-comment/<int:id>/', create_comment, name='create_comment'),
  path('delete-comment/<int:id>/', delete_comment, name='delete_comment'),
  
] 




