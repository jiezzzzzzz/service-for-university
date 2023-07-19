from django.contrib import admin
from .models import TrainingDiscipline, DirectionOfTraining


@admin.register(DirectionOfTraining)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'curator', 'direction_code']
    list_display_links = ['id']


@admin.register(TrainingDiscipline)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']
