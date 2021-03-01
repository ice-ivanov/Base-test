from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserRole


class UserRoleAdmin(admin.ModelAdmin):
    pass


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('id', 'username', 'role', 'notifications')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
