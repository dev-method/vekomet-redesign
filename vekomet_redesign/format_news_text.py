# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, '/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign')
sys.path.append("/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vekomet_redesign.settings")
import django
django.setup()
from bs4 import BeautifulSoup

from articles.models import NewArticle
art_list = NewArticle.objects.all()
for item in art_list:
    soup = BeautifulSoup(item.body, "lxml")
    content = soup.get_text()
    item.title_body = content[:150]
    item.save()

print ("excellent")