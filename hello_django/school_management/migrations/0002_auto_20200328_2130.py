# Generated by Django 3.0.4 on 2020-03-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='max_student',
            field=models.PositiveIntegerField(),
        ),
    ]
