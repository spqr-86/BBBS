from datetime import timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import BaseCommand
from django.utils.timezone import now
from django_apscheduler.jobstores import DjangoJobStore

from project.account.models import CustomUser
from project.api.utils.email import send_email
from project.project import settings


def send_notification():
    users = CustomUser.objects.all()
    week_time = now() + timedelta(days=7)
    for user in users:
        current_city = user.city
        print(user)
        print(user.city)
        events_by_city = current_city.events.all()
        print(events_by_city)
        for event in events_by_city:
            if now() < event.start_at <= week_time:
                send_email(
                    user.email,
                    f'Notification about event: {event.title}',
                    f'Hello, dont forget about {event.title}'
                )


class Command(BaseCommand):
    help = "Scheduler for sending email"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            send_notification,
            trigger=CronTrigger(second="*/86400"),
            max_instances=1,
            replace_existing=True,
        )

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
