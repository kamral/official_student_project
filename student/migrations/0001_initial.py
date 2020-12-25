# Generated by Django 3.1.4 on 2020-12-25 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs_number', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dorm_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('dorm_building', models.PositiveIntegerField(blank=True, null=True, verbose_name='Корпус')),
                ('floor', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_number', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField(blank=True, null=True)),
                ('student_name', models.CharField(max_length=100)),
                ('student_photo', models.ImageField(upload_to='', verbose_name='Фото студента')),
            ],
            options={
                'verbose_name': 'Номер комнаты',
                'verbose_name_plural': 'Номера комнат',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('telephone_number', models.CharField(max_length=100, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.direction')),
                ('dorm_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.dorm_room', verbose_name='Название общежития')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.faculty')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'student',
            },
        ),
    ]
