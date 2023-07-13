from django.db import models


class DirectionOfTraining(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField(default=12345)


class Curator(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    direction = models.OneToOneField(DirectionOfTraining, on_delete=models.CASCADE)


class TrainingDiscipline(models.Model):
    name = models.CharField(max_length=20)
    direction = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField(default='23.04.2003')
    directions = models.ManyToManyField(DirectionOfTraining, blank=True)
    disciplines = models.ManyToManyField(TrainingDiscipline, blank=True)


class StudyGroup(models.Model):
    direction = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)


