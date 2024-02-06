from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from mailing.models import Mailing, Logs


def send_mailing():
    current_time = timezone.localtime(timezone.now())
    mailing_list = Mailing.objects.all()
    for mailing in mailing_list:
        if mailing.time_start <= current_time < mailing.time_end:
            mailing.status = Mailing.STARTED
            mailing.save()
            for client in mailing.client.all():
                try:
                    send_mail(
                        subject=mailing.message.title,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )

                    log = Logs.objects.create(
                        last_try=mailing.time_start,
                        status_try='Отправлено',
                        mailing=mailing,
                        client=client
                    )
                    log.save()
                    return log

                except SMTPException as error:
                    log = Logs.objects.create(
                        last_try=mailing.time_to_send,
                        status_try='Ошибка',
                        mailling=mailing,
                        client=client,
                        answer=error
                    )
                    log.save()
                    return log

        else:
            mailing.status = Mailing.DONE
            mailing.save()
