from celery import Celery
from scraping import get_price
from database import save_toDb
from celery.schedules import crontab
from settings import REDIS_URL, GOOGLE_URL

app = Celery('tasks', broker=REDIS_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(crontab(minute='*/5'), scheduler_task.s(), name="every 5 minutes")
    sender.add_periodic_task(crontab(minute=0, hour="*"), scheduler_task.s(), name="every hour")

@app.task
def scheduler_task():
    price_value = get_price(GOOGLE_URL)
    save_toDb(price_value)
    
