from django.shortcuts import render
from positions.models import Metall, PriceData, PriceRare, Catalizator, TantalPositions, TantalDesc, TantalFoto
from pricelist.models import PriceSeo

# Create your views here.
def pricelist(request):
    pricelist_flag = "current"
    tantal_positions=TantalPositions.objects.all().order_by('priority')
    tantal_desc=TantalDesc.objects.all()
    tantal_fotos=TantalFoto.objects.all()
    catols=Catalizator.objects.all()
    group1=Metall.objects.filter(group=1).order_by('group_priority')
    group2=Metall.objects.filter(group=2).order_by('group_priority')
    group3=Metall.objects.filter(group=3).order_by('group_priority')
    group4=Metall.objects.filter(group=4).order_by('group_priority')
    group5=Metall.objects.filter(group=5).order_by('group_priority')
    group6=Metall.objects.filter(group=6).order_by('group_priority')
    group7=Metall.objects.filter(group=7).order_by('group_priority')
    group8=Metall.objects.filter(group=8).order_by('group_priority')
    group9=Metall.objects.filter(group=9).order_by('group_priority')
    group10=Metall.objects.filter(group=10).order_by('group_priority')
    group11=Metall.objects.filter(group=11).order_by('group_priority')
    raregroup1=Metall.objects.filter(group=101)
    raregroup2=Metall.objects.filter(group=102)
    raregroup3=Metall.objects.filter(group=103)
    pricedate=PriceData.objects.all()[0]
    pricerare=PriceRare.objects.all()
    seo=PriceSeo.objects.all()
    return render(request, 'pricelist/dev/pricelist.html', {'pricelist_flag': pricelist_flag, 'seo':seo,'group1':group1,'group2':group2,
                                                        'group3':group3,'group4':group4,'group5':group5, 'group6':group6,'group7':group7,'group8':group8,
                                                        'group9':group9,'group10':group10,'group11':group11,'pricedate':pricedate, 'pricerare':pricerare,
                                                        'raregroup1':raregroup1, 'raregroup2':raregroup2, 'raregroup3':raregroup3, 'catols':catols,
                                                         'tantal_positions':tantal_positions, 'tantal_desc':tantal_desc, 'tantal_fotos':tantal_fotos})

