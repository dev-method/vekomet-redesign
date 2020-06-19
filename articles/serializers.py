from articles.models import NewArticle
from rest_framework import serializers

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArticle
        fields = ('cover', 'title', 'body', 'title_body', 'author', 'pubdate', 'origin_title', 'origin_link', 'order', 'slug')

