# Generated by Django 4.2.3 on 2023-07-19 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='year_of_admission',
            new_name='date_of_admission',
        ),
    ]