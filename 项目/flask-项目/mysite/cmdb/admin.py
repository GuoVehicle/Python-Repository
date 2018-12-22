from django.contrib import admin

# Register your models here.
from . import models

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.UserInfo)