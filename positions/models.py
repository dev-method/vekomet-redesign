# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from positions.task import exel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
from django.contrib import admin
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from imagekit.admin import AdminThumbnail


# Create your models here.
class Metall(models.Model):
    seotitle=models.CharField('Seo-title', null=True, blank=True, max_length=300)
    en_seotitle = models.CharField('EN--->Seo-title', null=True, blank=True, max_length=300)
    seodescript=RichTextField('Seo-description', null=True, blank=True)
    en_seodescript = RichTextField('EN--->Seo-description', null=True, blank=True)
    seokeywords=RichTextField('Seo-keywords', null=True, blank=True)
    en_seokeywords = RichTextField('EN--->Seo-keywords', null=True, blank=True)
    canonicdes=models.BooleanField('Поставить каноническую ссылку на описание', default=True)
    canonicder=models.BooleanField('Поставить каноническую ссылку на справочник', default=False)
    indexdes=models.BooleanField('Noindex на описание', default=False)
    indexder=models.BooleanField('Noindex на справочник', default=False)
    title=models.CharField('Название', max_length=200)
    en_title = models.CharField('EN--->Название', max_length=200, null=True, blank=True)
    titlealt=models.CharField('Альтернативный заголовок страницы', max_length=200, null=True, blank=True)
    en_titlealt = models.CharField('EN--->Альтернативный заголовок страницы', max_length=200, null=True, blank=True)
    slug=models.SlugField(unique=True)
    alterslug=models.CharField('Адрес для замены описания на ссылку', max_length=1000, null=True, blank=True)
    price=models.CharField('Стоимость|Наличный расчет', max_length=200)
    price_bn = models.CharField('Стоимость|Безналичный расчет', max_length=200, null=True, blank=True)
    oldprice=models.CharField(max_length=200, null=True, blank=True)
    description1=RichTextUploadingField('Описание лома', null=True, blank=True)
    description_clear=RichTextUploadingField('Очищенное описание', null=True, blank=True)
    en_description1 = RichTextUploadingField('EN--->Описание лома', null=True, blank=True)
    description2 = RichTextUploadingField('Описание металла/сплава', null=True, blank=True)
    en_description2 = RichTextUploadingField('EN--->Описание металла/сплава', null=True, blank=True)
    description_amp = RichTextUploadingField('Описание для AMP страниц', null=True, blank=True)
    en_description_amp = RichTextUploadingField('EN--->Описание для AMP страниц', null=True, blank=True)
    add=models.DateTimeField('Добавлено',auto_now_add=True)
    visible=models.BooleanField('Видимость', default=True)
    priority=models.FloatField('Приоритет(для прайса на главной)', null=True,blank=True)
    group=models.IntegerField('Группа(для полного прайса)', null=True,blank=True)
    group_priority=models.FloatField('Порядок следования в группе', null=True,blank=True)
    tablepricegroup=models.IntegerField('Группа для формрования таблицы цен', null=True,blank=True)
    category = models.ForeignKey('MetallCategory', verbose_name="Категория металлов", blank=True, null=True, on_delete=models.CASCADE)
    vkid=models.IntegerField('Id товара в ВКОНТАКТЕ', null=True,blank=True)
    photo_grid=ProcessedImageField(verbose_name='Фото для справочника',upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90}, null=True, blank=True)
    photo_metall = ProcessedImageField(verbose_name='Фото для слайдера',upload_to='media/',
                                           processors=[ResizeToFill(370, 170)],
                                           format='JPEG',
                                           options={'quality': 90}, null=True, blank=True)
    photo_amp_1 = ProcessedImageField(verbose_name='Фото №1 для AMP-карусели', upload_to='media/',
                                     format='JPEG',
                                     processors=[ResizeToFill(400, 300)],
                                     options={'quality': 90}, null=True, blank=True)
    photo_amp_2 = ProcessedImageField(verbose_name='Фото №2 для AMP-карусели', upload_to='media/',
                                      format='JPEG',
                                      processors=[ResizeToFill(400, 300)],
                                      options={'quality': 90}, null=True, blank=True)
    photo_amp_3 = ProcessedImageField(verbose_name='Фото №3 для AMP-карусели', upload_to='media/',
                                      format='JPEG',
                                      processors=[ResizeToFill(400, 300)],
                                      options={'quality': 90}, null=True, blank=True)

    class Meta:
        verbose_name = ('Металл или сплав')
        verbose_name_plural = ('Металлы и сплавы')

    def __str__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, max_length=200)
        return super(Metall, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/metall/%s/" % self.slug

class MetallInline(admin.TabularInline):
    model = Metall

class MetallAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','visible',)
    tabular=[MetallInline]
    exclude = ('add','oldprice')
    search_fields = ['title']
    fieldsets = [
        (None,               {'fields': ['title','en_title','price','price_bn','visible','category']}),
        ('SEO', {'fields': ['seotitle','en_seotitle','seodescript','en_seodescript','seokeywords','en_seokeywords', 'titlealt','en_titlealt', 'canonicdes', 'canonicder', 'indexdes', 'indexder'], 'classes': ['collapse']}),
        ('Описание(лом+справочник)', {'fields': ['description1','description2'], 'classes': ['collapse']}),
        ('Описание англ.', {'fields': ['en_description1', 'en_description2'], 'classes': ['collapse']}),
        ('Группировка в прайсах', {'fields': ['priority','group', 'tablepricegroup', 'alterslug','group_priority'], 'classes': ['collapse']}),
        ('Фото', {'fields': ['photo_grid','photo_metall'], 'classes': ['collapse']}),
        ('ВКОНТАКТЕ', {'fields': ['vkid'], 'classes': ['collapse']}),
        ('AMP-страницы', {'fields': ['description_amp', 'en_description_amp','photo_amp_1','photo_amp_2', 'photo_amp_3'], 'classes': ['collapse']})
    ]

class PositionFoto(models.Model):
    foto=ProcessedImageField(verbose_name='Фото для позиций', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90}, blank=True, null=True)
    avatarfoto=ImageSpecField(source='foto',
                                      processors=[ResizeToFill(150, 150)],
                                      format='JPEG',
                                      options={'quality': 90})
    galleryfoto = ImageSpecField(source='foto',
                                 processors=[ResizeToFill(400, 250)],
                                 format='JPEG',
                                 options={'quality': 90})
    position=models.ForeignKey('Metall', verbose_name="Металл или сплав", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Фото для позиции')
        verbose_name_plural = ('Фото для позиции')

    def __str__(self):
        self.title = "Фото"
        return u'%s' % self.title

class FotoPositionInline(admin.TabularInline):
    model = PositionFoto

class FotoPositionAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',  'position')
    list_per_page = 20
    admin_thumbnail = AdminThumbnail(image_field='avatarfoto')
    tabular=[FotoPositionInline]

class PositionFooter(models.Model):
    text = RichTextUploadingField('Блок', null=True, blank=True)
    text_amp = RichTextUploadingField('Блок|AMP вариант', null=True, blank=True)
    class Meta:
        db_table = 'positionfooter'
        verbose_name = ('Блок контактов в описании позиции')
        verbose_name_plural = ('Блок контактов в описании позиции')

    def __str__(self):
        self.name='Содержание'
        return u'%s' % self.name

class MetallCategory(models.Model):
    name = models.CharField('Название категории', max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'metallcategory'
        verbose_name = ('Категория металлов')
        verbose_name_plural = ('Категория металлов')

    def __str__(self):
        return u'%s' % self.name


class PriceData(models.Model):
    pricedate=models.CharField('Прайс от...', max_length=50, null=True,blank=True)
    oldpricedate=models.CharField('Старая дата прайса', max_length=50, null=True,blank=True)

    class Meta:
        verbose_name = ('Дата изменения прайса')
        verbose_name_plural = ('Дата изменения прайса')

    def __str__(self):
        self.title="Дата прайса"
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        exel.delay()
        return super(PriceData, self).save(*args, **kwargs)


class PriceAdmin(admin.ModelAdmin):
    exclude=('oldpricedate',)

class PriceRare(models.Model):
    price = RichTextField('Прайс', null=True, blank=True)

    class Meta:
        verbose_name = ('Прайс редких металлов и сплавов')
        verbose_name_plural = ('Прайс редких металлов и сплавов')

    def __str__(self):
        self.title="Прайс редких металлов и сплавов"
        return u'%s' % self.title

class Catalizator(models.Model):
    title = models.CharField('Заголовок',max_length=400, null=True, blank=True)
    text1 = RichTextUploadingField('Текст по катализаторам', null=True, blank=True)
    text2 = RichTextUploadingField('Текст по катализаторам', null=True, blank=True)
    image1 = ProcessedImageField(verbose_name='Фото верх', upload_to='media/',
                                     format='JPEG',
                                     options={'quality': 90}, null=True, blank=True)
    image2 = ProcessedImageField(verbose_name='Фото низ', upload_to='media/',
                                format='PNG',
                                options={'quality': 90},
                                null=True, blank=True)

    class Meta:
        verbose_name = ('Катализаторы')
        verbose_name_plural = ('Катализаторы')

    def __str__(self):
        self.title="Описание для катализаторов"
        return u'%s' % self.title

class TantalPositions(models.Model):
    title = models.CharField('Название позиции',max_length=400, null=True, blank=True)
    price = models.CharField('Цена', max_length=200)
    priority = models.FloatField('Порядок следования', null=True, blank=True)

    class Meta:
        verbose_name = ('Тантал позиции')
        verbose_name_plural = ('Тантал позиции')

    def __str__(self):
        return u'%s' % self.title

class TantalDesc(models.Model):
    title = models.CharField('Заголовок к описанию',max_length=400, null=True, blank=True)
    sub1 = RichTextUploadingField('Текст | Абзац 1', null=True, blank=True)
    sub2 = RichTextUploadingField('Текст | Абзац 2', null=True, blank=True)
    image = ProcessedImageField(verbose_name='Фото для оформления', upload_to='media/',
                                 format='JPEG',
                                 options={'quality': 90}, null=True, blank=True)

    class Meta:
        verbose_name = ('Тантал описание')
        verbose_name_plural = ('Тантал описание')

    def __str__(self):
        self.text='Блок описания'
        return u'%s' % self.text

class TantalFoto(models.Model):
    foto=ProcessedImageField(verbose_name='Фото для позиции тантала', upload_to='media/',
                                           format='JPEG',
                                           options={'quality': 90}, blank=True, null=True)
    avatarfoto=ImageSpecField(source='foto',
                                      processors=[ResizeToFill(150, 150)],
                                      format='JPEG',
                                      options={'quality': 90})
    galleryfoto = ImageSpecField(source='foto',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 90})
    position=models.ForeignKey('TantalPositions', verbose_name="Тантал позиция", related_name='positions', related_query_name='position',on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Фото для позиций тантала')
        verbose_name_plural = ('Фото для позиций тантала')

    def __str__(self):
        self.title = "Фото"
        return u'%s' % self.title

class FotoTantalInline(admin.TabularInline):
    model = TantalFoto

class FotoTantalAdmin(admin.ModelAdmin):
    list_display = ('__str__','admin_thumbnail',  'position')
    list_per_page = 20
    admin_thumbnail = AdminThumbnail(image_field='avatarfoto')
    tabular=[FotoTantalInline]