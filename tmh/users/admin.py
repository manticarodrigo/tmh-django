from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class AbstractUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class AbstractUserAdmin(UserAdmin):
    form = AbstractUserChangeForm

    fieldsets = (
        ('Profile', { 'fields': ('image', 'city', 'state', ) }),
    ) + UserAdmin.fieldsets


admin.site.register(User, AbstractUserAdmin)


# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass