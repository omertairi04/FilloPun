from django.contrib import admin

from .models import Profile , Skills , Field , Message

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Skills)
admin.site.register(Field)
