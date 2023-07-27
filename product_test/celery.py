import os

from celery.app import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_test.settings')

# Create a Celery instance
app = Celery('product_task')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks.py files in all Django apps
app.autodiscover_tasks()
