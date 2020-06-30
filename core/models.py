# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class MainText(models.Model):
    title=models.CharField('Заголовок', max_length=400)
    en_title = models.CharField('EN--->Заголовок', max_length=400, null=True, blank=True)
    sub1=RichTextUploadingField('Текст в правой колонке', max_length=6000)
    en_sub1 = RichTextUploadingField('EN--->Текст в правой колонке', max_length=6000, blank=True, null=True)
    sub2=RichTextUploadingField('Текст в левой колонке', max_length=6000, blank=True, null=True)
    en_sub2 = RichTextUploadingField('EN--->Текст в левой колонке', max_length=6000, blank=True, null=True)
    sub1_turbo=RichTextUploadingField('Турбо-страницы | Первый абзац', max_length=6000, blank=True, null=True)
    sub2_turbo=RichTextUploadingField('Турбо-страницы | Второй абзац', max_length=6000, blank=True, null=True)
    sub1_amp=RichTextUploadingField('AMP-страницы|Первый абзац', max_length=6000, blank=True, null=True)
    sub2_amp=RichTextUploadingField('AMP-страницы|Второй абзац', max_length=6000, blank=True, null=True)

    class Meta:
        verbose_name = ('Основной текст')
        verbose_name_plural = ('Основной текст')

    def __str__(self):
        self.title="Текст на главной странице"
        return u'%s' % self.title

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

class MainTextBanner(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для баннерв - 992px',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    photo768 = ProcessedImageField(verbose_name='Фото для баннерв - 768px', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для баннерв - 576px', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90},null=True, blank=True)
    avatarphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Баннер раздела "О КОМПАНИИ"')
        verbose_name_plural = ('Баннер раздела "О КОМПАНИИ"')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title

class MainTextBannerInline(admin.TabularInline):
    model = MainTextBanner

class MainTextBannerAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarphoto')
    tabular=[MainTextBannerInline]


class MainPhoto(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для главного слайдера(992px)',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    photo768 = ProcessedImageField(verbose_name='Фото для главного слайдера(768px)', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90},null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для главного слайдера(576px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90},null=True, blank=True)
    avatarphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для главной карусели')
        verbose_name_plural = ('Фото для главной карусели')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title

class MainPhotoInline(admin.TabularInline):
    model = MainPhoto

class MainPhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarphoto')
    tabular=[MainPhotoInline]

class MainPhotoEn(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для главного слайдера',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    photo768 = ProcessedImageField(verbose_name='Фото для главного слайдера(768px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для главного слайдера(576px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    avatarphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для главной карусели-->англ.версия')
        verbose_name_plural = ('Фото для главной карусели-->англ.версия')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title

class MainPhotoEnInline(admin.TabularInline):
    model = MainPhoto

class MainPhotoEnAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarphoto')
    tabular=[MainPhotoEnInline]

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

class MPBanner(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для баннера(992px)',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    photo768 = ProcessedImageField(verbose_name='Фото для баннера(768px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    photo576 = ProcessedImageField(verbose_name='Фото для баннера(576px)', upload_to='media/',
                                   format='JPEG',
                                   options={'quality': 90}, null=True, blank=True)
    adminphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для баннера')
        verbose_name_plural = ('Фото для баннера')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title
class MPBannerInline(admin.TabularInline):
    model = MPBanner

class MPBannerAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='adminphoto')
    tabular=[MPBannerInline]

class MPBannerEN(models.Model):
    photo=ProcessedImageField(verbose_name='Фото для баннера',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90})
    adminphoto = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(150, 100)],
                                 format='JPEG',
                                 options={'quality': 50})

    class Meta:
        verbose_name = ('Фото для баннера англ.версия')
        verbose_name_plural = ('Фото для баннера англ.версия')

    def __str__(self):
        self.title="Фото"
        return u'%s' % self.title
class MPBannerEnInline(admin.TabularInline):
    model = MPBannerEN

class MPBannerEnAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='adminphoto')
    tabular=[MPBannerEnInline]


class FooterContacts(models.Model):
    block=RichTextUploadingField('Текст контактов', max_length=4000)
    en_block = RichTextUploadingField('EN--->Текст контактов', max_length=4000, null=True,blank=True)

    class Meta:
        verbose_name = ('Текст контактов в футере')
        verbose_name_plural = ('Текст контактов в футере')

    def __str__(self):
        self.title="Текст"
        return u'%s' % self.title

class MainSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    en_title = models.TextField('EN--->title', max_length=300, null=True, blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    en_description = models.TextField('EN--->description', max_length=1000, null=True, blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)
    en_keywords = models.TextField('EN--->keywords', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = ('SEO ДЛЯ ГЛАВНОЙ СТРАНИЦЫ')
        verbose_name_plural = ('SEO ДЛЯ ГЛАВНОЙ СТРАНИЦЫ')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title


