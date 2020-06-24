from django.contrib import admin
from wiki.models import WikiMaterials, WikiMaterialsAdmin, DirSeo

# Register your models here.
admin.site.register(DirSeo)
admin.site.register(WikiMaterials, WikiMaterialsAdmin)
