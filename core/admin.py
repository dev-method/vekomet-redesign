# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import MainPageText_P1, MainPageText_P2, Advantage, AdvantageAdmin
from core.models import MainSeo, MainPhoto, MainPhotoAdmin, TextSlider

# Register your models here.
admin.site.register(MainPageText_P1)
admin.site.register(MainPageText_P2); admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(MainPhoto, MainPhotoAdmin)
admin.site.register(TextSlider)
admin.site.register(MainSeo)