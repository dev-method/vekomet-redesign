# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail
from django.contrib import admin

# Create your models here.
class TextAnalysis(models.Model):
    sub1=RichTextField('Абзац1', max_length=6000)
    sub2=RichTextField('Абзац2', max_length=6000)

    class Meta:
        verbose_name = ('Текст на стр Анализ металла')
        verbose_name_plural = ('Текста на стр Анализ металла')

    def __str__(self):
        self.title="Текс для стр Анализ металла"
        return u'%s' % self.title


class AnalysisPhoto(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для слайдера',upload_to='media/',
                                           processors=[ResizeToFill(620, 300)],
                                           format='JPEG',
                                           options={'quality': 90})
    class Meta:
        verbose_name = ('Фото для слайдера на стр. Анализ металла')
        verbose_name_plural = ('Фото для слайдера на стр. Анализ металла')

    def __str__(self):
        self.title="Фото для слайдера на стр. Анализ металла"
        return u'%s' % self.title

class AnalizeBanner(models.Model):
    image=ProcessedImageField(verbose_name='Банер',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для баннера')
        verbose_name_plural = ('Фото для баннера')

    def __str__(self):
        self.title="Баннер"
        return u'%s' % self.title

class AnalizeBannerInline(admin.TabularInline):
    model = AnalizeBanner

class AnalizeBannerAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[AnalizeBannerInline]

class AnalysisSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title