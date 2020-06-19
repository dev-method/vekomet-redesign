from celery import shared_task
import subprocess
from django.core.mail import send_mail


@shared_task
def exel():
    subprocess.call('/var/www/vekomet.ru/VekometNew/bin/python3.6 /var/www/vekomet.ru/vekomet_v2/vekomet_v2/exceltask.py', shell=True)