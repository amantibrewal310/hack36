from django.contrib import admin
from accounts.models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FriendRequest)
admin.site.register(Message)
admin.site.register(Appoint)