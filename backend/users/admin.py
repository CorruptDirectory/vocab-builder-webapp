from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active', 'last_login', 'date_joined']
    list_filter = ['email', 'username', 'is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['last_login']

admin.site.register(CustomUser, CustomUserAdmin)
