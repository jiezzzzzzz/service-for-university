from django.db import models


class DirectionOfTraining(models.Model):
    name = models.CharField(
        verbose_name='Название направления',
        max_length=200,
    )
    curator = models.OneToOneField(
        verbose_name='Куратор',
        to='service.Curator',
        on_delete=models.CASCADE
    )
    direction_code = models.IntegerField(
        verbose_name='КОд дисциплины',
        default=1
    )

    class Meta:
        verbose_name = 'Направленние подготовки'
        verbose_name_plural = 'Направления подготовки'
        ordering = ['-title']

    def __str__(self):
        return f'{self.name}'


class TrainingDiscipline(models.Model):
    name = models.CharField(
        verbose_name='Название дисциплины',
        max_length=200)
    direction = models.ManyToManyField(
        DirectionOfTraining,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'
        ordering = ['-title']

    def __str__(self):
        return f'{self.name}'

