# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from core.models import MainPageText_P1, MainPageText_P2, Advantage, MainPhoto, MainSeo, TextSlider
from articles.models import NewArticle
from positions.models import Metall
from orders.models import Order
from vekomet_redesign import settings
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def mainpage(request):
    errors = []
    form = {}
    text_sliders = TextSlider.objects.all()
    sliders = MainPhoto.objects.all()
    try:
        main_text_p1 = MainPageText_P1.objects.all()[0]
    except IndexError:
        main_text_p1 = "Tекcт не найден"
    try:
        main_text_p2 = MainPageText_P2.objects.all()[0]
    except IndexError:
        main_text_p2 = "Tекcт не найден"
    seo = MainSeo.objects.all()
    first_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[0]
    second_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[1]
    third_new = NewArticle.objects.filter(category_id=2).order_by("-pubdate")[2]
    advantages_part1 = Advantage.objects.order_by("order")[0:4]
    advantages_part2 = Advantage.objects.order_by("order")[4:7]
    metalls = Metall.objects.order_by("priority")[:22]
    mainpage_flag = "current"
    mainpage_navigation_flag = True
    if request.POST:
        form['name'] = request.POST.get('name')
        form['contacts'] = request.POST.get('contacts')
        form['message'] = request.POST.get('message')
        if not form['contacts']:
            errors.append('Оставьте свои контакты')
        if not form['message']:
            errors.append('Укажите с каким вопросом вы к нам обратились?')
        if not request.recaptcha_is_valid:
            errors.append('Необходимо пройти каптчу')
        if not errors and request.recaptcha_is_valid:
            Order.objects.create(name=form['name'], contacts=form['contacts'], description=form['message'])
            messages.add_message(request, messages.INFO,
                                 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            return HttpResponseRedirect('/')
    return render(request, 'core/{}/mainpage.html'.format(settings.TEMP_PREFIX),{'errors': errors, 'form':form, 'mainpage_flag':mainpage_flag, 'mainpage_navigation_flag':mainpage_navigation_flag,
                                                     'main_text_p1': main_text_p1, 'main_text_p2': main_text_p2, 'first_new': first_new, 'second_new':second_new,
                                                     'third_new':third_new, 'advantages_part1': advantages_part1, 'advantages_part2': advantages_part2, 'seo': seo,
                                                     'metalls': metalls, 'sliders': sliders, 'text_sliders': text_sliders})

def en_mainpage(request):
    en_lang_flag = True
    return render(request, 'core/{}/mainpage.html',{'en_lang_flag': en_lang_flag})

def intaractive_map(request):
    return render(request, 'core/dev/intaractive-map.html',{})

def calculator(request):
    return render(request, 'core/dev/calculator.html',{})