from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from tmh.core.models.user import User
from tmh.core.models.project import Project
from tmh.core.models.detail import ProjectDetail
from tmh.core.models.item import ProjectItem
from tmh.core.models.message import ProjectMessage

class AbstractUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class AbstractUserAdmin(UserAdmin):
    form = AbstractUserChangeForm

    fieldsets = (
        ('Profile', { 'fields': ('image', 'city', 'state', ) }),
    ) + UserAdmin.fieldsets

admin.site.register(User, AbstractUserAdmin)
admin.site.register(Project)
admin.site.register(ProjectDetail)
admin.site.register(ProjectItem)
admin.site.register(ProjectMessage)
