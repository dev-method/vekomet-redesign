from django import template
from articles.models import NewArticle
from vekomet_redesign import settings
register = template.Library()

@register.inclusion_tag('core/news-sidebar.html')
def show_news():
    debug = settings.DEBUG
    news = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0:3]
    return {'news': news, 'debug': debug}