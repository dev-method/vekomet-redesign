from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from positions.models import Metall
from articles.models import NewArticle
from wiki.models import DirSeo, DirBanner, WikiMaterials
from django.views.decorators.clickjacking import xframe_options_exempt


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
    return render(request,'wiki/dev/wiki.html',{'wiki_flag': wiki_flag, 'list':metall_list, 'seo':seo, 'materials':materials, 'metalls':metalls})

@xframe_options_exempt
def wiki_summaterials(request, slug):
    first_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0]
    second_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[1]
    third_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[2]
    wiki_flag = "current"
    slug=slug
    metallslug=Metall.objects.get(slug=slug)
    id=metallslug.id
    materials=WikiMaterials.objects.filter(position_id=id).order_by('-pubdate')
    paginator = Paginator(materials, 10)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request,'wiki/dev/wiki-item-summaterials.html',{'first_new': first_new, 'second_new':second_new,
                                                                  'third_new':third_new,'materials':list, 'wiki_flag': wiki_flag,
                                                                  'metallslug':metallslug})
@xframe_options_exempt
def wiki_item_material(request, id):
    first_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0]
    second_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[1]
    third_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[2]
    wiki_flag = "current"
    id=id
    material=WikiMaterials.objects.get(id=id)
    return render(request, 'wiki/dev/wiki-item-material.html', {'first_new': first_new, 'second_new':second_new,
                                                                  'third_new':third_new, 'material': material, 'wiki_flag': wiki_flag})


