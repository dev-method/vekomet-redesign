# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VKMessage(models.Model):
    userid=models.CharField('ID пользователя', max_length=200)
    f_name = models.CharField('Имя пользователя', max_length=1000, null=True, blank=True)
    l_name = models.CharField('Фамилия пользователя', max_length=1000, null=True, blank=True)
    is_read=models.BooleanField('Прочитано ли сообщение', default=False)
    image_url=models.CharField('Url аватара', max_length=1000, null=True, blank=True)
    title=models.CharField('Тема сообщения', max_length=1000)
    date=models.TextField('Дата сообщения',max_length=6000)
    body=models.TextField('Дата сообщения',max_length=6000)
    idmes=models.CharField('ID сообщения', max_length=200, null=True, blank=True)
    post=models.BooleanField('Отослано ли письмо?', default=False)

    class Meta:
        verbose_name = ('Личное сообщение VK')
        verbose_name_plural = ('Личные сообщения VK')

    def __str__(self):
        self.mes="Сообщение"
        return u'%s' % self.mes

class VKMessageGroup(models.Model):
    userid=models.CharField('ID пользователя', max_length=200)
    f_name = models.CharField('Имя пользователя', max_length=1000, null=True, blank=True)
    l_name = models.CharField('Фамилия пользователя', max_length=1000, null=True, blank=True)
    is_read=models.BooleanField('Прочитано ли сообщение', default=False)
    image_url=models.CharField('Url аватара', max_length=1000, null=True, blank=True)
    title=models.CharField('Тема сообщения', max_length=1000)
    date=models.TextField('Дата сообщения',max_length=6000)
    body=models.TextField('Дата сообщения',max_length=6000)
    idmes=models.CharField('ID сообщения', max_length=200, null=True, blank=True)
    post = models.BooleanField('Отослано ли письмо?', default=False)

    class Meta:
        verbose_name = ('Групповое сообщение VK')
        verbose_name_plural = ('Групповые сообщения VK')

    def __str__(self):
        self.mes="Сообщение"
        return u'%s' % self.mes