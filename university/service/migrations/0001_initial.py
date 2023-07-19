# Generated by Django 4.2.3 on 2023-07-19 14:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('gender', models.BooleanField(blank=True, choices=[(True, 'Мужчина'), (False, 'Женщина')], verbose_name='Пол')),
                ('age', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)], verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Куратор',
                'verbose_name_plural': 'Кураторы',
                'ordering': ['-surname'],
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('students_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_service.directionoftraining', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('gender', models.BooleanField(blank=True, choices=[(True, 'Мужчина'), (False, 'Женщина')], verbose_name='Пол')),
                ('date_of_birth', models.DateField(default='23.04.2003', verbose_name='Дата рождения')),
                ('year_of_admission', models.DateField(auto_now_add=True, verbose_name='Дата поступления')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.studygroup', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ['-group'],
            },
        ),
    ]
