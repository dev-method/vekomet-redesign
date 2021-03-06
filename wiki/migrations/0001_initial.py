# Generated by Django 3.0.2 on 2020-02-12 17:05

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='media/', verbose_name='Банер')),
            ],
            options={
                'verbose_name': 'Фото для баннера',
                'verbose_name_plural': 'Фото для баннера',
            },
        ),
        migrations.CreateModel(
            name='DirSeo',
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
            name='WikiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Тип материала')),
                ('icon', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/', verbose_name='Иконка материала')),
            ],
            options={
                'verbose_name': 'Тип материала для справочника',
                'verbose_name_plural': 'Тип материала для справочника',
                'db_table': 'wiki_category',
            },
        ),
        migrations.CreateModel(
            name='WikiMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seotitle', models.CharField(blank=True, max_length=300, null=True, verbose_name='Seo-title')),
                ('seodescript', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Seo-description')),
                ('seokeywords', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Seo-keywords')),
                ('slug', models.SlugField(unique=True)),
                ('video_url', models.CharField(blank=True, max_length=1000, verbose_name='URL видео')),
                ('host_file', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Файл на хостинге')),
                ('file_url', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка на внешний файл')),
                ('title', models.CharField(max_length=1000, verbose_name='Название текста')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст материала')),
                ('author', models.BooleanField(default=False, verbose_name='Авторский материал')),
                ('origin_title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название источника заимствования')),
                ('origin_link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на источник заимствования')),
                ('pubdate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время публикации')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.WikiCategory', verbose_name='Тип материала')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='positions.Metall', verbose_name='К какой позиции')),
            ],
            options={
                'verbose_name': 'Материал для справочника',
                'verbose_name_plural': 'Материалы для справочника',
            },
        ),
    ]
