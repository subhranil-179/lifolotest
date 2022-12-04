from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from accounts.models import User, UserProfile

# Register your models here.

class UserAdmin(AbstractUserAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
