from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Curator(models.Model):
    GENDER_CHOICES = [
        (True, 'Мужчина'),
        (False, 'Женщина'),
    ]
    name = models.CharField(
        verbose_name='Имя',
        max_length=200
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=200
    )
    gender = models.BooleanField(
        verbose_name='Пол',
        choices=GENDER_CHOICES,
        blank=True
    )
    age = models.IntegerField(
        verbose_name='Возраст',
        blank=True,
        validators=[
            MinValueValidator(18),
            MaxValueValidator(120)
        ]
    )

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'
        ordering = ['-surname']

    def __str__(self):
        return f'{self.name} {self.surname}'


class StudyGroup(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    direction = models.ForeignKey(
        verbose_name='Направление',
        to='admin_service.DirectionOfTraining',
        on_delete=models.CASCADE
    )
    students_count = models.IntegerField(
        verbose_name='',
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20)
        ]
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-name']

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    GENDER_CHOICES = [
        (True, 'Мужчина'),
        (False, 'Женщина'),
    ]
    name = models.CharField(
        verbose_name='Имя',
        max_length=200
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=200
    )
    gender = models.BooleanField(
        verbose_name='Пол',
        choices=GENDER_CHOICES,
        blank=True
    )
    group = models.ForeignKey(
        StudyGroup,
        verbose_name='Группа',
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        default='23.04.2003'
    )
    year_of_admission = models.DateField(
        verbose_name='Дата поступления',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-group']

    def __str__(self):
        return f'{self.name} {self.surname}'

