# Generated by Django 3.0.2 on 2020-02-12 17:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя клиента')),
                ('contacts', models.CharField(max_length=600, verbose_name='Контактные данные')),
                ('description', models.TextField(max_length=4000, verbose_name='Запрос')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='OrdersSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=300, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('keywords', models.TextField(blank=True, max_length=1000, null=True, verbose_name='keywords')),
            ],
            options={
                'verbose_name': 'SEO',
                'verbose_name_plural': 'SEO',
            },
        ),
        migrations.CreateModel(
            name='OrderText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(max_length=6000, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст на стр Сообщения',
                'verbose_name_plural': 'Текст на стр Сообщения',
            },
        ),
    ]
