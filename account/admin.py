from django.contrib import admin
from .models import UserBase


@admin.register(UserBase)
class UserBaseAdmin(admin.ModelAdmin):
    pass