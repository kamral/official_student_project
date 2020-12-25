# Generated by Django 3.1.4 on 2020-12-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbiturientHelpInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100, verbose_name='Название компании')),
                ('body', models.TimeField(verbose_name='Содержимое текста')),
                ('date_of_foundation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo_manager', models.CharField(max_length=100, verbose_name='Директор компании')),
                ('backend_developer', models.CharField(max_length=100, verbose_name='Бек разработчик')),
                ('frontent_developer', models.CharField(max_length=100, verbose_name='Фронт разработчик')),
                ('support_service', models.CharField(max_length=100, verbose_name='Служба поддержки')),
            ],
        ),
        migrations.CreateModel(
            name='Ourpartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя партнера')),
            ],
        ),
        migrations.CreateModel(
            name='StudentHelpInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
