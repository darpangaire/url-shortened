from django.urls import path
from .views import ChannelViewSet

urlpatterns = [
  path('',ChannelViewSet.as_view(),name='channel'),
  
] 

