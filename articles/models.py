# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
from bs4 import BeautifulSoup
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib import admin
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


def replace_tag_content(soup, *tags):
    for tag in tags:
        for item in soup.find_all(tag):
                content = item.string
                item.replace_with(content)
    return soup

# Create your models here.
class Article(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    seodescript = RichTextField('Seo-description', null=True, blank=True)
    seokeywords = RichTextField('Seo-keywords', null=True, blank=True)
    title = models.CharField('Название статьи', max_length=400)
    slug = models.SlugField(unique=True)
    body = RichTextField('Текст статьи', null=True, blank=True)
    pubdate = models.DateTimeField('Добавлено', auto_now_add=True, null=True, blank=True)
    photo = ProcessedImageField(verbose_name='Фото для оформления', upload_to='media/',
                                processors=[ResizeToFill(250, 150)],
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/articles/%s/" % self.slug


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('slug', 'pubdate',)
    fieldsets = [
        ('Статья', {'fields': ['title', 'body', 'photo']}),
        ('SEO', {'fields': ['seotitle', 'seodescript', 'seokeywords'], 'classes': ['collapse']})

    ]


class NewArticle(models.Model):
    seotitle = models.CharField('Seo-title', null=True, blank=True, max_length=300)
    seodescript = RichTextField('Seo-description', null=True, blank=True)
    seokeywords = RichTextField('Seo-keywords', null=True, blank=True)
    slug = models.SlugField(unique=True)
    cover = ProcessedImageField(verbose_name='Обложка статьи/новости', upload_to='media/',
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    cover_turbo = ImageSpecField(source='cover',
                                 processors=[ResizeToFill(400, 250)],
                                 format='JPEG',
                                 options={'quality': 90})
    thumb = ImageSpecField(source='cover',
                            processors=[ResizeToFill(350, 250)],
                            format='JPEG',
                            options={'quality': 90})
    title = models.CharField('Название статьи/новости', max_length=1000)
    body = RichTextUploadingField('Текст статьи/новости', null=True, blank=True)
    title_body = RichTextUploadingField('Текст в афише статьи', null=True, blank=True)
    author = models.BooleanField('Авторская статья/новость', default=False)
    origin_title = models.CharField('Название источника заимствования', max_length=1000, null=True, blank=True)
    origin_link = models.CharField('Ссылка на источник заимствования', max_length=1000, null=True, blank=True)
    pubdate = models.DateTimeField('Время публикации', auto_now_add=True, null=True, blank=True)
    order = models.FloatField('Порядок группировки', null=True, blank=True)
    post=models.BooleanField("Опубликовано в авто режиме", default=False)
    post_custom = models.BooleanField("Задержать публикацию", default=False)
    category = models.ForeignKey('ArticleCategory', verbose_name="Тип статьи", blank=True, null=True,
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'СТАТЬЯ | НОВОСТЬ'
        verbose_name_plural = 'СТАТЬИ | НОВОСТИ'

    def __str__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.title_body:
            soup = BeautifulSoup(self.body, "lxml")
            content =soup.get_text(strip=True)
            self.title_body = content[:150]
        return super(NewArticle, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.category_id==2:
            return "/news/%s/" % self.slug
        else:
            return "/articles/%s/" % self.slug

class NewArticlesInline(admin.TabularInline):
    model = NewArticle

class NewArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    exclude = ('slug', 'pubdate',)
    tabular=[NewArticlesInline]
    search_fields = ['title']
    fieldsets = [
        ('Статья', {'fields': ['cover', 'title', 'body', 'title_body', 'author', 'origin_title', 'origin_link', 'order',
                               'post_custom', 'category']}),
        ('SEO', {'fields': ['seotitle', 'seodescript', 'seokeywords'], 'classes': ['collapse']})

    ]

class ArticleCategory(models.Model):
    name=models.CharField('Тип',  max_length=300, null=True,blank=True)

    class Meta:
        db_table = 'article_category'
        verbose_name = ('Тип материала(статья/новость)')
        verbose_name_plural = ('Тип материала(статья/новость)')

    def __str__(self):
        return '%s' % self.name

class ArticlesSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO ДЛЯ РАЗДЕЛА "СТАТЬИ"')
        verbose_name_plural = ('SEO ДЛЯ РАЗДЕЛА "СТАТЬИ"')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title

class NewsSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO ДЛЯ РАЗДЕЛА "НОВОСТИ"')
        verbose_name_plural = ('SEO ДЛЯ РАЗДЕЛА "НОВОСТИ"')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title