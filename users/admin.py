from django.contrib import admin

from .models import Profile, BusinessProfile , Skills , Field

admin.site.register(Profile)
admin.site.register(BusinessProfile)
admin.site.register(Skills)
admin.site.register(Field)
