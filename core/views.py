# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from core.models import MainPageText_P1, MainPageText_P2, Advantage
from articles.models import NewArticle
from positions.models import Metall

# Create your views here.
def mainpage(request):
    try:
        main_text_p1 = MainPageText_P1.objects.all()[0]
    except IndexError:
        main_text_p1 = "Tекcт не найден"
    try:
        main_text_p2 = MainPageText_P2.objects.all()[0]
    except IndexError:
        main_text_p2 = "Tекcт не найден"
    first_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0]
    second_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[1]
    third_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[2]
    advantages_part1 = Advantage.objects.order_by("order")[0:4]
    advantages_part2 = Advantage.objects.order_by("order")[4:7]
    metalls = Metall.objects.order_by("priority")[:22]
    mainpage_flag = "current"
    mainpage_navigation_flag = True
    return render(request, 'core/dev/mainpage.html',{'mainpage_flag':mainpage_flag, 'mainpage_navigation_flag':mainpage_navigation_flag,
                                                     'main_text_p1': main_text_p1, 'main_text_p2': main_text_p2, 'first_new': first_new, 'second_new':second_new,
                                                     'third_new':third_new, 'advantages_part1': advantages_part1, 'advantages_part2': advantages_part2,
                                                     'metalls': metalls})

def intaractive_map(request):
    return render(request, 'core/dev/intaractive-map.html',{})

def calculator(request):
    return render(request, 'core/dev/calculator.html',{})