from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Channels(models.Model):
  name = models.CharField(max_length=255,unique=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_channels")
  members = models.ManyToManyField(User,through="ChannelsMemberShip",related_name='channels')
  
  class Meta:
    verbose_name_plural ='channels'
    
  def __str__(self):
    return self.name
  

class Post(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = "post"
  
  def __str__(self):
    return self.title
  
class PostImages(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='images')
  images = models.ImageField(upload_to='post/')
  
  class Meta:
    verbose_name_plural= 'PostImages'
  
  def __str__(self):
    return f"Image for {self.post.title}"
  
  
class ChannelsMemberShip(models.Model):
  channel = models.ForeignKey(Channels,on_delete=models.CASCADE,related_name="memberships")
  member = models.ForeignKey(User,on_delete=models.CASCADE,related_name='joined_channels')
  joined_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    unique_together = ('channel','member') # Prevent duplicate joins
    
  def __str__(self):
    return f"{self.member.username} in {self.channel.name}"
  
  


  

    
  

  
  