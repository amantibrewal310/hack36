from django.contrib import admin

from accounts.models import *

from accounts.models import UserProfile, Skills


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FriendRequest)
admin.site.register(Message)
admin.site.register(Appoint)
admin.site.register(Skills)

