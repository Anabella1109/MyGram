from django.contrib import admin
from .models import Image, Profile , Comment

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
