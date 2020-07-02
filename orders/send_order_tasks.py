from celery import shared_task
from django.core.mail import send_mail

@shared_task(acks_late=True)
def send_order(name, contacts, description):
    subject="Имя:  "+name+"\n"+"Телефон или почта:  "+contacts+"\n"+"Сообщение:  "+description
    send_mail('Запрос на обратную связь', subject, 'admin@vekomet.ru', ['vekokat@gmail.com'], fail_silently=False)
    print("success")