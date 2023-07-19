from django.contrib import admin
from .models import TrainingDiscipline, DirectionOfTraining


@admin.register(TrainingDiscipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'curator', 'direction_code']
    list_display_links = ['id']


@admin.register(DirectionOfTraining)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']