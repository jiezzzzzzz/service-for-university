from rest_framework import serializers
from .models import DirectionOfTraining, TrainingDiscipline


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDiscipline
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionOfTraining
        fields = '__all__'
