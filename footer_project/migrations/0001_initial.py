# Generated by Django 3.1.4 on 2021-01-03 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Company_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя ')),
            ],
        ),
        migrations.CreateModel(
            name='Opportunities_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Ourpartners_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ourpartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя партнера')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footer_project.ourpartners_category')),
            ],
        ),
        migrations.CreateModel(
            name='Oportunities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=100, verbose_name='Ответ')),
                ('body', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footer_project.opportunities_category')),
            ],
        ),
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, verbose_name='Содержимое текста')),
                ('date_of_foundation', models.DateTimeField(auto_now_add=True)),
                ('ceo_manager', models.CharField(blank=True, max_length=100, verbose_name='Директор компании')),
                ('backend_developer', models.CharField(blank=True, max_length=100, verbose_name='Бек разработчик')),
                ('frontent_developer', models.CharField(blank=True, max_length=100, verbose_name='Фронт разработчик')),
                ('support_service', models.CharField(blank=True, max_length=100, verbose_name='Служба поддержки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footer_project.about_company_category')),
            ],
        ),
    ]
