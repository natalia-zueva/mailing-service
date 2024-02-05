from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timedelta

from django.utils import timezone

from mailing.models import Mailing, Logs


def send_mailing(mailing: Mailing):
    current_time = timezone.localtime(timezone.now())
    if mailing.time_start <= current_time < mailing.time_end:
        mailing.status = Mailing.STARTED
        mailing.save()
        for message in mailing.messages.all():
            for client in mailing.clients.all():
                try:
                    result = send_mail(
                        subject=message.title,
                        message=message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )
                    log = Logs.objects.create(
                        time_try=mailing.time_start,
                        status_try=result,
                        response_server='OK',
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                    return log

                except SMTPException as error:
                    log = Logs.objects.create(
                        time_try=mailing.time_start,
                        status_try=False,
                        response_server=error,
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                return log

    else:
        mailing.status = Mailing.DONE
        mailing.save()
