from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'mobile')

    fieldsets = (
        ('General Info', {'fields': ('username', 'password'), }),
        ('Personal info', {'fields': ('first_name', 'email', 'mobile', 'profile_image')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (None, {'fields': ('last_login', 'date_joined')}),
    )


# admin.site.register(User, UserAdmin)
admin.site.register(User, CustomUserAdmin)
