# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from orders.send_order_tasks import send_order
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Order(models.Model):
    name=models.CharField('Имя клиента', max_length=200)
    contacts=models.CharField('Контактные данные', max_length=600)
    description=models.TextField('Запрос',max_length=4000 )

    class Meta:
        verbose_name = ('ЗАЯВКА')
        verbose_name_plural = ('ЗАЯВКИ')

    def __str__(self):
        return u'%s' % self.name


class OrderText(models.Model):
    text=RichTextUploadingField('Текст', max_length=6000)

    class Meta:
        verbose_name = ('Текст на стр Сообщения')
        verbose_name_plural = ('Текст на стр Сообщения')

    def __str__(self):
        self.title="Текст на стр Сообщения"
        return u'%s' % self.title

class OrdersSeo(models.Model):
    title=models.TextField('title', max_length=300, null=True,blank=True)
    description=models.TextField('description', max_length=1000, null=True,blank=True)
    keywords=models.TextField('keywords', max_length=1000, null=True,blank=True)

    class Meta:
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')

    def __str__(self):
        self.title="SEO"
        return u'%s' % self.title
"""
@receiver(post_save, sender=Order)
def new_order_sendmail(sender, instance, created, raw, using, **kwargs):
    send_order(instance.name, instance.contacts, instance.description)
"""





