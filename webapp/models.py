from django.db import models

# Create your models here.
class WebSite(models.Model):
    youtube_link = models.URLField(blank=True,null=True)
    telegram_link = models.URLField(blank=True,null=True)
    twitter_link = models.URLField(blank=True,null=True)
    facebook_link = models.URLField(blank=True,null=True)


    class Meta:
        verbose_name_plural = "Web Site Info"
