# Generated by Django 3.1.4 on 2021-01-11 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Общеобразовательная система')),
            ],
        ),
        migrations.CreateModel(
            name='General_education_system',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo/')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('date_of_foundation', models.DateTimeField(auto_now_add=True)),
                ('filial', models.CharField(blank=True, max_length=100, verbose_name='Филиал университета')),
                ('history_of_university', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General_education_system.category_education')),
            ],
        ),
    ]
