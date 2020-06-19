from django.contrib import admin
from wiki.models import WikiMaterials, WikiMaterialsAdmin

# Register your models here.
admin.site.register(WikiMaterials, WikiMaterialsAdmin)
