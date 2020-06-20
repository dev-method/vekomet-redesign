from django.shortcuts import render
from articles.models import NewArticle, ArticlesSeo, NewsSeo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from articles.serializers import ArticlesSerializer
from vekomet_redesign import settings
# Create your views here.

def articles(request):
    seo = ArticlesSeo.objects.all()
    materials_flag = "current"
    return render(request, 'articles/{}/articles.html'.format(settings.TEMP_PREFIX), {'materials_flag':materials_flag, 'seo': seo})


def articles_item(request,slug):
    materials_flag = "current"
    material=NewArticle.objects.filter(category_id=1).get(slug=slug)
    return render(request, 'articles/{}/material-item.html'.format(settings.TEMP_PREFIX), {'material': material, 'materials_flag':materials_flag})

def news(request):
    seo = NewsSeo.objects.all()
    materials_flag = "current"
    return render(request, 'articles/{}/news.html'.format(settings.TEMP_PREFIX), {'materials_flag':materials_flag, 'seo': seo})


def news_item(request,slug):
    materials_flag = "current"
    material=NewArticle.objects.filter(category_id=2).get(slug=slug)
    return render(request, 'articles/{}/material-item.html'.format(settings.TEMP_PREFIX), {'material': material, 'materials_flag':materials_flag})

@api_view(['GET'])
def articles_collection(request):
    if request.method == 'GET':
        articles = NewArticle.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def articles_news_collection(request):
    if request.method == 'GET':
        articles = NewArticle.objects.filter(category_id=2).order_by("-pubdate")
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def articles_theme_collection(request):
    if request.method == 'GET':
        articles = NewArticle.objects.filter(category_id=1).order_by("-pubdate")
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

