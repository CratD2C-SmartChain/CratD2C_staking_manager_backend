import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
app = Celery("src")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update_active_validators_amounts": {
        "task": "update_active_validators_amounts",
        "schedule": crontab(
            minute="*/1"
        ),
    },
    "update_archived_validators": {
        "task": "update_archived_validators",
        "schedule": crontab(
            minute="*/1"
        ),
    },
    "update_total_delegators": {
        "task": "update_total_delegators",
        "schedule": crontab(
            minute="*/1"
        ),
    },
}
