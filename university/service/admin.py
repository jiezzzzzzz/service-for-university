from django.contrib import admin
from .models import Curator, StudyGroup, Student


@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'gender', 'age']
    list_display_links = ['id']


@admin.register(StudyGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'direction', 'students_count']
    list_display_links = ['id']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'group', 'date_of_birth', 'date_of_admission']
    list_display_links = ['id']
