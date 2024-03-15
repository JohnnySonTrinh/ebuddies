from django.contrib import admin

# Register your models here.

from .models import Thread, Topic, Message

admin.site.register(Thread)
admin.site.register(Topic)
admin.site.register(Message)
