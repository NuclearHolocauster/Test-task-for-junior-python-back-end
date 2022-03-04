from django.contrib import admin
from .models import Student, Group


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'create_at')
    list_display_links = ('id', 'first_name')
    search_fields = ('id', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'create_at')


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'create_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'course', 'create_at')


admin.site.register(Student, StudentsAdmin)
admin.site.register(Group, GroupsAdmin)
