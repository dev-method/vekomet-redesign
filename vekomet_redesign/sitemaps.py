from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from positions.models import Metall
from wiki.models import WikiMaterials
from articles.models import NewArticle
from django.db.models import Q


class PosSitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return Metall.objects.all()

class WikiSitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        materials = WikiMaterials.objects.all()
        metalls = Metall.objects.order_by('title')
        id_list = []
        if materials:
            for i in materials:
                id = i.position_id
                if id in id_list:
                    pass
                else:
                    id_list.append(id)
        metall_list = []
        for i in metalls:
            if i.id in id_list:
                if i in metall_list:
                    pass
                else:
                    metall_list.append(i)
        return metall_list

    def location(self, item):
        return "/wiki/%s/" % item.slug

class WikiItemSitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return WikiMaterials.objects.filter(Q(category_id=1) | Q(category_id=2))

class ArtSitemap(Sitemap):
    changefreq='daily'
    priority=0.5

    def items(self):
        return NewArticle.objects.all()

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main', 'contacts', 'directory','pricelist','analysis']
    def location(self, item):
        return reverse(item)
