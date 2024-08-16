import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
app = Celery("src")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
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
