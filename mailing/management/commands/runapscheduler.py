
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore


from mailing.services import send_mailing

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_mailing,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        )
        logger.info("Added message 'send_mailing'.")

        # scheduler.add_job(
        #     send_message,
        #     trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        # )
        # logger.info("Added job 'my_job'.")
        #
        # scheduler.add_job(
        #     send_message,
        #     trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        # )
        # logger.info("Added job 'my_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
