from django.contrib import admin

#importing 'Post' model made in models.py file within blog
from .models import Post



admin.site.register(Post)