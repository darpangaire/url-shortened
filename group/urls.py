from django.urls import path
from .views import ChannelCreateAPIView,ChannelMemberShipCreateAPIView,PostCreateAPIView

urlpatterns = [
  path('',ChannelCreateAPIView.as_view(),name='createchannel'),
  path('join-channels/',ChannelMemberShipCreateAPIView.as_view(),name='join-channels'),
  path('create-posts/',PostCreateAPIView.as_view(),name='create-posts'),
  
] 



