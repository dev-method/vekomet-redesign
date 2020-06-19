# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail
from django.contrib import admin


# Create your models here.

class ContactsText(models.Model):
    sub1=RichTextUploadingField('Текст', help_text="Введите текст, отображаемый на странице Контакты", max_length=6000)
    en_sub1 = RichTextUploadingField('Текст( EN )', help_text="Английская версия текста, отображаемого на странице Контакты", max_length=6000, null=True,blank=True)

    class Meta:
        verbose_name = ('Текст на стр Контакты')
        verbose_name_plural = ('Текст на стр Контакты')

    def __str__(self):
        self.title="Содержание текста"
        return u'%s' % self.title

class ContTextAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['sub1']}),
        ('АНГЛИЙСКАЯ ВЕРСИЯ', {'fields': ['en_sub1'], 'classes': ['collapse']})
    ]

class ContactsBanner(models.Model):
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

class ContactsBannerInline(admin.TabularInline):
    model = ContactsBanner

class ContactsBannerAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[ContactsBannerInline]

class ContactsSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    en_title = models.TextField('EN--->title', max_length=300, null=True, blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    en_description = models.TextField('EN--->description', max_length=1000, null=True, blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)
    en_keywords = models.TextField('EN--->keywords', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title
