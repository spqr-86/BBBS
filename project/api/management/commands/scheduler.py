from datetime import timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.timezone import now
from django_apscheduler.jobstores import DjangoJobStore

from api.models import Event
from api.utils.email import send_email

User = get_user_model()


def send_notification():
    events = Event.objects.filter(
        start_at__gt=now(),
        start_at__lt=now() + timedelta(hours=24)
    )
    for event in events:
        users = User.objects.filter(events=event)
        for user in users:
            send_email(
                user.email,
                f'Напоминание о событии: {event.title}',
                f'Здравствуйте!\n\n \
                 Не забудьте посетить событие "{event.title}".\n \
                 Начало {event.start_at.strftime("%d.%m.%Y в %H:%M")}'
            )


class Command(BaseCommand):
    help = 'Scheduler for sending email'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        scheduler.add_job(
            send_notification,
            trigger=CronTrigger(day='*/1'),
            id='Events reminder',
            max_instances=1,
            replace_existing=True,
        )

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
