from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
def get_default_channel_images():
  return f"channels/dummy_image.png"


class Channels(models.Model):
  name = models.CharField(max_length=255,unique=True)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_channels")
  members = models.ManyToManyField(User,through="ChannelsMemberShip",related_name='channels',null=True,blank=False)
  image  = models.ImageField(upload_to='channels/',null=True,default=get_default_channel_images,blank=True)
  
  class Meta:
    verbose_name_plural ='channels'
    
  def __str__(self):
    return self.name
  
  def save(self,*args,**kwargs):
    if not self.image:
      self.image = get_default_channel_images()
    super().save(*args,**kwargs)
    

  
  

class Post(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  channel = models.ForeignKey(Channels,on_delete=models.CASCADE,related_name='posts',null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = "post"
  
  def __str__(self):
    return self.title
  
class PostImages(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='images')
  images = models.ImageField(upload_to='post/',null=True,blank=True)
  
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
  
 
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=255)  # For anonymous users
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) 

  
  def __str__(self):
    return self.name
  



