# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from PIL import Image
from vekomet_redesign import settings
import os, time
from celery import shared_task
from django.db.models.signals import post_save
from django.dispatch import receiver
if settings.DEBUG:
    media_path = '/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign/files/media/media/'
    app_url = '/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign'
else:
    media_path = '/usr/src/vekomet.ru/vekomet_redesign/media/media/'
    app_url = '/usr/src/vekomet.ru/vekomet_redesign'

# Create your models here.


class MainPageText_P1(models.Model):
    title=models.CharField('Заголовок', max_length=400)
    en_title = models.CharField('EN--->Заголовок', max_length=400, null=True, blank=True)
    sub1=RichTextUploadingField('Текст в правой колонке', max_length=6000)
    en_sub1 = RichTextUploadingField('EN--->Текст в правой колонке', max_length=6000, blank=True, null=True)
    sub2=RichTextUploadingField('Текст в левой колонке', max_length=6000, blank=True, null=True)
    en_sub2 = RichTextUploadingField('EN--->Текст в левой колонке', max_length=6000, blank=True, null=True)

    class Meta:
        verbose_name = ('О КОМПАНИИ | ТЕКСТ | ЧАСТЬ 1')
        verbose_name_plural = ('О КОМПАНИИ | ТЕКСТ | ЧАСТЬ 1')

    def __str__(self):
        self.text="Редактировать текст"
        return u'%s' % self.text

class MainPageText_P2(models.Model):
    sub1=RichTextUploadingField('Текст в правой колонке', max_length=6000)
    en_sub1 = RichTextUploadingField('EN--->Текст в правой колонке', max_length=6000, blank=True, null=True)
    sub2=RichTextUploadingField('Текст в левой колонке', max_length=6000, blank=True, null=True)
    en_sub2 = RichTextUploadingField('EN--->Текст в левой колонке', max_length=6000, blank=True, null=True)

    class Meta:
        verbose_name = ('О КОМПАНИИ | ТЕКСТ | ЧАСТЬ 2')
        verbose_name_plural = ('О КОМПАНИИ | ТЕКСТ | ЧАСТЬ 2')

    def __str__(self):
        self.text="Редактировать текст"
        return u'%s' % self.text

class TextSlider(models.Model):
    sentence = models.CharField('Фраза для слайдера', max_length=6000, blank=True, null=True)
    en_sentence = RichTextUploadingField('EN--->Фраза для слайдера', max_length=6000, blank=True, null=True)

    class Meta:
        verbose_name = ('ТЕКСТОВЫЙ СЛАЙДЕР')
        verbose_name_plural = ('ТЕКСТОВЫЙ СЛАЙДЕР')

    def __str__(self):
        return u'%s' % self.sentence

class MainPhoto(models.Model):
    photo=ProcessedImageField(verbose_name='ФОТО | JPEG | 1920х500', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    photo_low = ImageSpecField(source='photo',
                               format='JPEG',
                               options={'quality': 1})
    photo_webp = models.CharField(verbose_name='ФОТО | WEBP | 1920х500',
                                  max_length=600, null=True, blank=True)
    photo_jp2 = models.CharField(verbose_name='ФОТО | JPEG 2000 | 1920х500', max_length=600, null=True, blank=True)
    photo768 = ProcessedImageField(verbose_name='ФОТО | JPEG | 768х', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},null=True, blank=True)
    photo_768_low = ImageSpecField(source='photo768',
                               format='JPEG',
                               options={'quality': 1})
    photo_768_webp = models.CharField(verbose_name='ФОТО | WEBP | 768х',
                                  max_length=600, null=True, blank=True)
    photo_768_jp2 = models.CharField(verbose_name='ФОТО | JPEG 2000 | 768х', max_length=600, null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для главного слайдера(576px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90},null=True, blank=True)
    photo_576_low = ImageSpecField(source='photo576',
                                   format='JPEG',
                                   options={'quality': 1})
    photo_576_webp = models.CharField(verbose_name='ФОТО | WEBP | 576х',
                                      max_length=600, null=True, blank=True)
    photo_576_jp2 = models.CharField(verbose_name='ФОТО | JPEG 2000 | 576х', max_length=600, null=True, blank=True)
    avatarphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('ГЛАВНЫЙ СЛАЙДЕР | ФОТО')
        verbose_name_plural = ('ГЛАВНЫЙ СЛАЙДЕР | ФОТО')

    def __str__(self):
        self.title="Изображение"
        return u'%s' % self.title

class MainPhotoInline(admin.TabularInline):
    model = MainPhoto

class MainPhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarphoto')
    tabular=[MainPhotoInline]
    fieldsets = [
        ('ФОТО | РАЗМЕР 1920x', {'fields': ['photo', 'photo_webp', 'photo_jp2']}),
        ('ФОТО | РАЗМЕР 768x', {'fields': ['photo768', 'photo_768_webp', 'photo_768_jp2'],
                 'classes': ['collapse']}),
        ('ФОТО | РАЗМЕР 576x', {'fields': ['photo576', 'photo_576_webp', 'photo_576_jp2'], 'classes': ['collapse']}),
    ]
'''
@shared_task(acks_late=True)
def mainphoto_alter_formats(pk):
    time.sleep(1)
    mainphoto_item = MainPhoto.objects.get(pk=pk)
    origin_name = os.path.basename(mainphoto_item.photo.url)
    clear_name = origin_name.split('.')[0]
    Image.open(media_path+origin_name).save(media_path+clear_name+'.webp', 'webp', quality='70')
    Image.open(media_path + origin_name).save(media_path + clear_name + '.jpx', quality_mode='dB', quality_layers=[34])
    mainphoto_item.photo_webp = '/media/media/' + clear_name+'.webp'
    mainphoto_item.photo_jp2 = '/media/media/' + clear_name + '.jpx'
    origin_name_768 = os.path.basename(mainphoto_item.photo768.url)
    clear_name_768 = origin_name_768.split('.')[0]
    Image.open(media_path + origin_name_768).save(media_path + clear_name_768 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_768).save(media_path + clear_name_768 + '.jpx', quality_mode='dB', quality_layers=[34])
    mainphoto_item.photo_768_webp = '/media/media/' + clear_name_768 + '.webp'
    mainphoto_item.photo_768_jp2 = '/media/media/' + clear_name_768 + '.jpx'
    origin_name_576 = os.path.basename(mainphoto_item.photo576.url)
    clear_name_576 = origin_name_576.split('.')[0]
    Image.open(media_path + origin_name_576).save(media_path + clear_name_576 + '.webp', 'webp', quality='70')
    Image.open(media_path + origin_name_576).save(media_path + clear_name_576 + '.jpx', quality_mode='dB',
                                                  quality_layers=[34])
    mainphoto_item.photo_576_webp = '/media/media/' + clear_name_576 + '.webp'
    mainphoto_item.photo_576_jp2 = '/media/media/' + clear_name_576 + '.jpx'
    mainphoto_item.save()

@receiver(post_save, sender= MainPhoto)
def methods_image(instance, **kwargs):
    if instance.photo_webp and instance.photo_jp2:
        if not os.path.isfile(app_url+instance.photo_webp):
            mainphoto_alter_formats(instance.pk)
        elif not os.path.isfile(app_url+instance.photo_jp2):
            mainphoto_alter_formats(instance.pk)
        else:
            pass
    elif instance.photo:
        mainphoto_alter_formats(instance.pk)
    else:
        pass
'''

class Advantage(models.Model):
    image=ProcessedImageField(verbose_name='Фото',upload_to='media/',
                                           format='PNG',
                                           options={'quality': 90})
    avatarimage = ImageSpecField(source='image',
                                 processors=[ResizeToFill(50, 50)],
                                 format='JPEG',
                                 options={'quality': 50})
    text=models.TextField('Текст', max_length=1000)
    en_text = models.TextField('EN--->Текст', max_length=1000, blank=True, null=True)
    order = models.IntegerField('Порядок следования на страницк', blank=True, null=True)

    class Meta:
        verbose_name = ('ПРЕИМУЩЕСТВА | БЛОК')
        verbose_name_plural = ('ПРЕИМУЩЕСТВА | БЛОКИ')

    def __str__(self):
        self.title="Блок преимущества"
        return u'%s' % self.title

class AdvantageInline(admin.TabularInline):
    model = Advantage

class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('text', '__str__', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[AdvantageInline]


class FooterPhoto(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для нижнего слайдера(992px)',upload_to='media/',
                                           processors=[ResizeToFill(370, 170)],
                                           format='JPEG',
                                           options={'quality': 90})
    photo768 = ProcessedImageField(verbose_name='Фото для нижнего слайдера(768px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для нижнего слайдера(576px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    adminphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для нижнего слайдера')
        verbose_name_plural = ('Фото для нижнего слайдера')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title
class FooterPhotoInline(admin.TabularInline):
    model = FooterPhoto

class FooterPhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='adminphoto')
    tabular=[FooterPhotoInline]

class MainSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    en_title = models.TextField('EN--->title', max_length=300, null=True, blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    en_description = models.TextField('EN--->description', max_length=1000, null=True, blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)
    en_keywords = models.TextField('EN--->keywords', max_length=1000, null=True, blank=True)
    op_graph_photo = ProcessedImageField(verbose_name='ФОТО ДЛЯ OPENGRAPH', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    class Meta:
        verbose_name = ('SEO | OPENGRAPH ДЛЯ ГЛАВНОЙ СТРАНИЦЫ')
        verbose_name_plural = ('SEO | OPENGRAPH ДЛЯ ГЛАВНОЙ СТРАНИЦЫ')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title


