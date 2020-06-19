# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import MainText, MainPageText_P1, MainPageText_P2, MainTextBanner, MainTextBannerAdmin, Advantage, AdvantageAdmin
# Register your models here.
admin.site.register(MainText)
admin.site.register(MainPageText_P1)
admin.site.register(MainPageText_P2)
admin.site.register(MainTextBanner, MainTextBannerAdmin)
admin.site.register(Advantage, AdvantageAdmin)
