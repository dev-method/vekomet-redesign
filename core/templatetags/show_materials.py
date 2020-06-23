from django import template
from articles.models import NewArticle
register = template.Library()

@register.inclusion_tag('core/news-sidebar.html')
def show_news():
    news = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0:3]
    return {'news': news}