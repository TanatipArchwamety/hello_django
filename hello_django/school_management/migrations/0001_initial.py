# Generated by Django 3.0.4 on 2020-03-28 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(default='school/no-img.jpg', upload_to='school/')),
                ('name', models.CharField(max_length=20)),
                ('max_student', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(default='student/no-img.jpg', upload_to='student/')),
                ('student_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_management.School')),
            ],
        ),
    ]
