import os
import smtplib

import pytz
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from main.models import Mailing, TryToSend
from datetime import timedelta
from django.core.cache import cache

from main.models import ClientMessage, ServiceClient
from config.settings import CACHE_ENABLED


def send_mails():
    """
    Функция отправки рассылок
    """
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(is_active=True)

    for mailing in mailings:
        if mailing.next_send_time is None:
            mailing.next_send_time = mailing.start_time
            mailing.status = Mailing.STARTED
            mailing.save()
        # Если достигли end_date, завершить рассылку
        if current_datetime >= mailing.end_time:
            mailing.status = Mailing.COMPLETED
            mailing.save()
            continue  # Пропустить отправку, если end_date достигнут

        # Проверить, нужно ли отправить сообщение в текущий момент времени
        if mailing.end_time >= current_datetime and mailing.next_send_time >= mailing.start_time:
            mailing.status = Mailing.STARTED
            clients = mailing.client_list.all()
            try:
                server_response = send_mail(
                    subject=mailing.client_message.title,
                    message=mailing.client_message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in clients],
                    fail_silently=False,
                )
                TryToSend.objects.create(status=TryToSend.DONE,
                                         server_response=server_response,
                                         mailing_list=mailing, )
            except smtplib.SMTPException as e:
                TryToSend.objects.create(status=TryToSend.FALL,
                                         server_response=str(e),
                                         mailing_list=mailing, )
            print("до :", mailing.next_send_time)
            # Обновление времени следующей отправки
            if mailing.periodicity == Mailing.DAILY:
                mailing.next_send_time += timedelta(days=1)
                mailing.start_time = mailing.next_send_time
            elif mailing.periodicity == Mailing.WEEKLY:
                mailing.next_send_time += timedelta(weeks=1)
                mailing.start_time = mailing.next_send_time
            elif mailing.periodicity == Mailing.MONTHLY:
                mailing.next_send_time += timedelta(days=30)
                mailing.start_time = mailing.next_send_time

            mailing.save()
            print("после :", mailing.next_send_time)


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Проверка, добавлена ли задача уже
    if not scheduler.get_jobs():
        scheduler.add_job(send_mails, 'interval', minutes=1)

    if not scheduler.running:
        scheduler.start()


def get_message_list_from_cache():
    messages = ClientMessage.objects.all()
    if not CACHE_ENABLED:
        return messages
    key = 'clientmessage_list'
    message = cache.get(key)
    if message is None:
        cache.set(key, messages)
        return messages
    return message


def get_client_list_from_cache():
    clients = ServiceClient.objects.all()
    if not CACHE_ENABLED:
        return clients
    key = 'serviceclient_list'
    client = cache.get(key)
    if client is None:
        cache.set(key, clients)
        return clients
    return client



###def send_mails():
#zone = pytz.timezone(settings.TIME_ZONE)
#current_datetime = datetime.now(zone)
#mailings = Mailing.objects.filter(start_time__lte=current_datetime) #.filter(
# статус_рассылки__in=[список_статусов])

#for mailing in mailings:
#print(mailing.__dict__)
#send_mail(
#subject=theme,
#message=text,
#from_email=settings.EMAIL_HOST_USER,
#recipient_list=[client.email for client in mailing.клиенты.all()]
#)
#if mailing.periodicity == Mailing.DAILY:
#next_date = mailing.start_time + timedelta(days=1)
#elif mailing.periodicity == Mailing.WEEKLY:
#next_date = mailing.start_time + timedelta(days=7)
#elif mailing.periodicity == Mailing.MONTHLY:
#next_date = mailing.start_time + timedelta(days=30)
#print("до :", mailing.start_time)
#mailing.start_time = next_date
#mailing.save()
#print("после :", mailing.start_time)
