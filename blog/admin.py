from django.contrib import admin
from .models import Blog, FeedBacks, Callback, CarMark, Car
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

admin.site.register(Blog)
admin.site.register(FeedBacks)
admin.site.register(Callback)
admin.site.register(Car)
admin.site.register(CarMark)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'phone_number', 'is_superuser', 'bio', 'birthdate')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'phone_number', 'is_superuser', 'bio', 'birthdate', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'username', 'phone_number', 'is_superuser')
         }),
    )
    search_fields = ('username', 'phone_number', 'birthdate', 'bio', 'email')
    ordering = ('username', 'phone_number', 'birthdate')

admin.site.register(CustomUser, CustomUserAdmin)