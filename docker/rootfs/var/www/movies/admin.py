from django.contrib import admin
from .models import comment_for_movie,video


# Register your models here.

admin.site.register(comment_for_movie)
admin.site.register(video)
