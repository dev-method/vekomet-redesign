# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from core import views as coreviews
from django.contrib.sitemaps.views import sitemap
from orders import views as orders_views
from pricelist import views as price_views
from positions import views as position_views
from analysis import views as analize_views
from articles import views as articles_views
from wiki import views as wiki_views
from contacts import views as contacts_views
from vekomet_redesign.sitemaps import StaticViewSitemap,PosSitemap, ArtSitemap, WikiSitemap, WikiItemSitemap


sitemaps={
    'static':StaticViewSitemap,
    'positions':PosSitemap(),
    'articles':ArtSitemap(),
    'wiki':WikiSitemap(),
    'wiki-item': WikiItemSitemap()
}

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('', coreviews.mainpage, name="main"),
    path('en/', coreviews.en_mainpage, name="en_main"),
    path('api-auth/', include('rest_framework.urls')),
    path('articles/api/total/', articles_views.articles_collection, name="articles_collection"),
    path('articles/api/news/', articles_views.articles_news_collection, name="articles_news_collection"),
    path('articles/api/topics/', articles_views.articles_theme_collection, name="articles_theme_collection"),
    path('map/', coreviews.intaractive_map, name="intaractive-map"),
    path('modal-form-handler/', orders_views.modal_form_handler, name="modal_form_handler"),
    path('sliding-form-handler/', orders_views.sliding_form_handler, name="sliding_form_handler"),
    path('main-form-handler/', orders_views.main_form_handler, name="main_form_handler"),
    path('metall-calculator/', coreviews.calculator, name="calculator"),
    path('pricelist/', price_views.pricelist, name="pricelist"),
    path('orders/api/collection/', orders_views.orders_api, name="orders_api"),
    path('metall/<slug:slug>/', position_views.position_detail, name='position_detail'),
    path('metall-analysis/', analize_views.analysis, name="analysis"),
    path('articles/', articles_views.articles, name='articles'),
    path('articles/<slug:slug>/', articles_views.articles_item, name='articles_item'),
    path('news/', articles_views.news, name="news"),
    path('news/<slug:slug>/', articles_views.news_item, name="news_item"),
    path('wiki/', wiki_views.catalog, name="directory"),
    path('wiki/<slug:slug>/',wiki_views.wiki_summaterials, name='wiki_summaterials'),
    path('wiki/materials/<int:id>/', wiki_views.wiki_item_material, name="wiki_item_material"),
    path('contacts/', contacts_views.contacts, name="contacts"),
    path('en/contacts/', contacts_views.en_contacts, name="en_contacts"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
