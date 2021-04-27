from django.contrib import admin
from .models import WebSite

# Register your models here.

@admin.register(WebSite)
class WEADMIN(admin.ModelAdmin):
    list_display = [
        'youtube_link',
        'telegram_link',
        'twitter_link',
        'facebook_link',
    ]