# myapp/tasks.py

from celery import shared_task
from datetime import datetime
from bus.models import Bus

@shared_task
def create_something_on_specific_day(day):
    if datetime.today().date() == day:
       # MyModel.objects.create(name='My Object')
       pass
