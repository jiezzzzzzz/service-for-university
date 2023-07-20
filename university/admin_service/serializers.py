from rest_framework import serializers
from .models import DirectionOfTraining, TrainingDiscipline


class TrainingDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDiscipline
        fields = '__all__'


class DirectionOfTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionOfTraining
        fields = '__all__'
