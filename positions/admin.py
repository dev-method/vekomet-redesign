from django.contrib import admin
from positions.models import Metall, MetallAdmin, PositionFoto, FotoPositionAdmin
from positions.models import PriceData, PriceAdmin, PriceRare
from positions.models import TantalPositions, TantalDesc, TantalFoto, FotoTantalAdmin

# Register your models here.

admin.site.register(Metall, MetallAdmin)
admin.site.register(PositionFoto, FotoPositionAdmin)
admin.site.register(PriceData, PriceAdmin)
admin.site.register(PriceRare)
admin.site.register(TantalPositions)
admin.site.register(TantalFoto, FotoTantalAdmin)



