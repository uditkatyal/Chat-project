from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Post)
# admin.site.register(Message)
# admin.site.register(StarredPost)
# admin.site.register(StarredMessage)