from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'role',
        'email'
    )

    list_filter = ('role',)

    search_fields = (
        'username',
        'first_name',
        'last_name'
    )