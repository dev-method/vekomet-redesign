# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class ModAppMess(models.Model):
    name=models.CharField('Имя клиента', max_length=200, blank=True, null=True)
    phone=models.CharField('Телефон', max_length=600, blank=True, null=True)
    mail = models.CharField('Почта', max_length=1000, blank=True, null=True)
    message =models.TextField('Сообщение',max_length=5000, blank=True, null=True)

    class Meta:
        verbose_name = ('Заявка')
        verbose_name_plural = ('Заявки')

    def __str__(self):
        return u'%s' % self.name






