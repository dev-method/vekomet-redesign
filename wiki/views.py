from django.shortcuts import render
from django.core.paginator import Paginator
from positions.models import Metall
from wiki.models import DirSeo, WikiMaterials
from django.views.decorators.clickjacking import xframe_options_exempt
from vekomet_redesign import settings


# Create your views here.
def catalog(request):
    wiki_flag = "current"
    seo=DirSeo.objects.all()
    materials=WikiMaterials.objects.all()
    metalls=Metall.objects.order_by('title')
    id_list = []
    if materials:
        for i in materials:
            id = i.position_id
            if id in id_list:
                pass
            else:
                id_list.append(id)
    metall_list=[]
    for i in metalls:
        if i.id in id_list:
            if i in metall_list:
                pass
            else:
                metall_list.append(i)
    return render(request,'wiki/{}/wiki.html'.format(settings.TEMP_PREFIX),{'wiki_flag': wiki_flag, 'list':metall_list, 'seo':seo, 'materials':materials, 'metalls':metalls})

@xframe_options_exempt
def wiki_summaterials(request, slug):
    wiki_flag = "current"
    slug=slug
    metallslug=Metall.objects.get(slug=slug)
    id=metallslug.id
    materials=WikiMaterials.objects.filter(position_id=id).order_by('-pubdate')
    paginator = Paginator(materials, 10)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request,'wiki/{}/wiki-item-summaterials.html'.format(settings.TEMP_PREFIX),{'materials':list,
                                                                                              'wiki_flag': wiki_flag,
                                                                                              'metallslug':metallslug})
@xframe_options_exempt
def wiki_item_material(request, id):
    wiki_flag = "current"
    id=id
    material=WikiMaterials.objects.get(id=id)
    return render(request, 'wiki/{}/wiki-item-material.html'.format(settings.TEMP_PREFIX), {'material': material,
                                                                                            'wiki_flag': wiki_flag})


