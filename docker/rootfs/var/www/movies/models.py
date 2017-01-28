from __future__ import unicode_literals

from django.db import models
from vms.settings import STATIC_URL
# Create your models here.

class comment_for_movie(models.Model):
    user_name=models.CharField(max_length=255,default="",blank=True)
    user_subject=models.CharField(max_length=255,default="",blank=True)
    movie_name = models.CharField(max_length=255,default="",blank=True)
    user_comment=models.TextField(default="",blank=True)
    user_mail=models.EmailField(blank=True)
    #date=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.user_comment
class video(models.Model):

    video_name = models.CharField(max_length=255,blank=True)
    video_type=models.CharField(max_length=50)
    views=models.IntegerField(default=0)
    video_img=models.ImageField(upload_to='Images',name='',blank=True,null=True)
    video_file=models.FileField(upload_to='Videos',name='')
    video_rate=models.FloatField(default=0,max_length=5.0)
    upload_time=models.DateTimeField()
    video_year=models.CharField(max_length=4,blank=True)
    def __str__(self):
        return self.video_name
