# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class PriceSeo(models.Model):
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

