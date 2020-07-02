from django.shortcuts import render
from orders.serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from orders.models import Order
from rest_framework.response import Response
from django.contrib import messages
from django.http import HttpResponseRedirect
from orders.decorators import check_recaptcha
# Create your views here.

@api_view(['GET', 'POST'])
def orders_api(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@check_recaptcha
def main_form_handler(request):
    error_flag = True
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')
        form['contacts'] = request.POST.get('contacts')
        form['message'] = request.POST.get('message')
        if not form['contacts']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите ваши контакты для обратной связи')
        if not form['message']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите c каким вопросом вы к нам обратились')
        if not request.recaptcha_is_valid:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Поставьте галочку, чтобы мы убедились, что вы не робот')
        if error_flag:
            Order.objects.create(name=form['name'], contacts=form['contacts'], description=form['message'])
            messages.add_message(request, messages.INFO,
                                 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

@check_recaptcha
def modal_form_handler(request):
    error_flag = True
    form = {}
    if request.POST:
        form['name'] = request.POST.get('top_name')
        form['contacts'] = request.POST.get('top_contacts')
        form['message'] = request.POST.get('top_message')
        if not form['contacts']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите ваши контакты для обратной связи')
        if not form['message']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите c каким вопросом вы к нам обратились')
        if not request.recaptcha_is_valid:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Поставьте галочку, чтобы мы убедились, что вы не робот')
        if error_flag:
            Order.objects.create(name=form['name'], contacts=form['contacts'], description=form['message'])
            messages.add_message(request, messages.INFO,
                                 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

@check_recaptcha
def sliding_form_handler(request):
    error_flag = True
    form = {}
    if request.POST:
        form['name'] = request.POST.get('slide_name')
        form['contacts'] = request.POST.get('slide_contacts')
        form['message'] = request.POST.get('slide_message')
        if not form['contacts']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите ваши контакты для обратной связи')
        if not form['message']:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Укажите c каким вопросом вы к нам обратились')
        if not request.recaptcha_is_valid:
            error_flag = False
            messages.add_message(request, messages.INFO,
                                 'Поставьте галочку, чтобы мы убедились, что вы не робот')
        if error_flag:
            Order.objects.create(name=form['name'], contacts=form['contacts'], description=form['message'])
            messages.add_message(request, messages.INFO,
                                 'Ваша заявка отправлена, в ближайшее время с Вами свяжутся наши специалисты.')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')