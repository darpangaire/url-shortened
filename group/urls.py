from django.urls import path
from .views import ChannelCreateAPIView,ChannelMemberShipCreateAPIView,PostCreateAPIView,home

urlpatterns = [
  path('create-channel',ChannelCreateAPIView.as_view(),name='createchannel'),
  path('join-channels/',ChannelMemberShipCreateAPIView.as_view(),name='join-channels'),
  path('create-posts/',PostCreateAPIView.as_view(),name='create-posts'),
  
  path('',home,name='home'),
  
] 



