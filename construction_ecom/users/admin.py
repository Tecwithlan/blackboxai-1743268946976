from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'business_name', 'business_type', 'approved')
    list_filter = ('business_type', 'approved')
    fieldsets = UserAdmin.fieldsets + (
        ('Business Information', {'fields': ('business_name', 'business_type', 'tax_id', 'tax_exempt', 'approved')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
