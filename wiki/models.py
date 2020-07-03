# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail
from django.contrib import admin



# Create your models here.

class DirBanner(models.Model):
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

class DirBannerInline(admin.TabularInline):
    model = DirBanner

class DirBannerAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='avatarimage')
    tabular=[DirBannerInline]


class DirSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)
    op_graph_photo = ProcessedImageField(verbose_name='ФОТО ДЛЯ OPENGRAPH', upload_to='media/',
                                         format='JPEG',
                                         options={'quality': 90}, null=True, blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title

class WikiMaterials(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    seodescript = RichTextField('Seo-description', null=True, blank=True)
    seokeywords = RichTextField('Seo-keywords', null=True, blank=True)
    slug = models.SlugField(unique=True)
    video_url=models.CharField('URL видео', max_length=1000, blank=True)
    host_file = models.FileField("Файл на хостинге", upload_to='uploads/', null=True, blank=True)
    file_url = models.CharField('Ссылка на внешний файл', max_length=1000, blank=True)
    title = models.CharField('Название текста', max_length=1000)
    body = RichTextUploadingField('Текст материала', null=True, blank=True)
    author = models.BooleanField('Авторский материал', default=False)
    origin_title = models.CharField('Название источника заимствования', max_length=1000, null=True, blank=True)
    origin_link = models.CharField('Ссылка на источник заимствования', max_length=1000, null=True, blank=True)
    pubdate = models.DateTimeField('Время публикации', auto_now_add=True, null=True, blank=True)
    position = models.ForeignKey('positions.Metall', verbose_name="К какой позиции", blank=True, null=True,
                                 on_delete=models.CASCADE)
    category = models.ForeignKey('WikiCategory', verbose_name="Тип материала", blank=True, null=True,
                                 on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'МАТЕРИАЛ ДЛЯ СПРАВОЧНИКА'
        verbose_name_plural = 'МАТЕРИАЛЫ ДЛЯ СПРАВОЧНИКА'

    def __str__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(WikiMaterials, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.category_id == 1 or self.category_id == 2:
            return "/wiki/materials/%s/" %self.id

class WikiMaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_position', 'category')
    def get_position(self, obj):
        return obj.position.title
    get_position.short_description = "Позиция"
    search_fields = ['title']
    exclude = ('slug', 'pubdate',)
    fieldsets = [
        (None,    {'fields': ['title','position', 'category']}),
        ('SEO',   {'fields': ['seotitle', 'seodescript', 'seokeywords'], 'classes': ['collapse']}),
        ('ТЕКСТ', {'fields': ['body', 'author', 'origin_title', 'origin_link']}),
        ('ВИДЕО', {'fields': ['video_url'], 'classes': ['collapse']}),
        ('ФАЙЛЫ', {'fields': ['host_file', 'file_url'], 'classes': ['collapse']}),
    ]

class WikiCategory(models.Model):
    name=models.CharField('Тип материала',  max_length=300, null=True,blank=True)
    icon = ProcessedImageField(verbose_name='Иконка материала', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    thumb = ImageSpecField(source='icon',
                           processors=[ResizeToFill(50, 50)],
                           format='JPEG',
                           options={'quality': 90})
    class Meta:
        db_table = 'wiki_category'
        verbose_name = ('Тип материала для справочника')
        verbose_name_plural = ('Тип материала для справочника')

    def __str__(self):
        return '%s' % self.name