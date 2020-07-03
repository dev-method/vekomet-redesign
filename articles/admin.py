from django.contrib import admin
from articles.models import NewArticle, NewArticleAdmin
from articles.models import ArticlesSeo, NewsSeo

# Register your models here.

admin.site.register(NewArticle, NewArticleAdmin)
admin.site.register(ArticlesSeo)
admin.site.register(NewsSeo)

