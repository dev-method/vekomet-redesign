# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, '/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign')
sys.path.append("/home/vladimir/Projects/vekomet-django-react-redesign/vekomet_redesign")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vekomet_redesign.settings")
import django
django.setup()
from bs4 import BeautifulSoup

from positions.models import Metall
met_list = Metall.objects.all()
for item in met_list:
    soup = BeautifulSoup(item.description1, "lxml")
    for tag in soup.findAll("span"):
        if tag["style"]:
            del tag["style"]
            tag["style"] = 'color:#678595'
    item.description1 = str(soup.select_one("body"))
    item.save()
print ("excellent")