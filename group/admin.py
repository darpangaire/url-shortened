from django.contrib import admin
from django.utils.html import format_html
from .models import Channels,Post,PostImages,ChannelsMemberShip

# Register your models here.
class ChannelsAdmin(admin.ModelAdmin):
  list_display = ["id","name","created_at","admin"]
  list_filter = ["name"]
  fieldsets = []
  search_fields = ["name"]
  ordering = ["name","admin"]
  filter_horizontal = []
  readonly_fields = ["created_at"]
  
  def save_model(self, request, obj, form, change):
    if not obj.pk:
      obj.admin = request.user
    super().save_model(request, obj, form, change)
    
class PostAdmin(admin.ModelAdmin):
  list_display = ['id','title','created_at']
  fieldsets=[]
  search_fields = ["title"]
  
class PostImagesAdmin(admin.ModelAdmin):
  list_display = ['id','post__title','images_preview']
  readonly_fields = ['images_preview']
  search_fields = ['post__title']
  
  def images_preview(self,obj):
    if obj.images:
      return format_html("<img src='{}' width='100' />",obj.images.url)
    
    return "No Images"
  
  images_preview.short_description = "preview"
  
class ChannelsMemberShipAdmin(admin.ModelAdmin):
  list_display = ['id','channel__name']
  

admin.site.register(ChannelsMemberShip,ChannelsMemberShipAdmin)
admin.site.register(PostImages,PostImagesAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Channels,ChannelsAdmin)
  

