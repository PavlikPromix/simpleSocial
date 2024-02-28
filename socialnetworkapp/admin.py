from django.contrib import admin
from .models import User, Post, Subscription, Like, Comment

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(Like)
admin.site.register(Comment)
