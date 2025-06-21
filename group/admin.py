from django.contrib import admin
from .models import Channels

# Register your models here.
class ChannelsAdmin(admin.ModelAdmin):
  list_display = ["id","name","created_at","created_by"]
  list_filter = ["name"]
  fieldsets = []
  search_fields = ["name"]
  ordering = ["name","created_by"]
  filter_horizontal = []
  readonly_fields = ["created_at","created_by"]
  
admin.site.register(Channels,ChannelsAdmin)
  
  
