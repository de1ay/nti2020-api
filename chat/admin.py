from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(ChatGroup)
admin.site.register(ChatUsers)
admin.site.register(ChatMessage)
