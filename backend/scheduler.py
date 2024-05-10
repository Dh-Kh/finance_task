from celery import Celery
from scraping import get_price
from database import save_toDb
from celery.schedules import crontab

app = Celery('tasks', broker='redis://redis:6379/')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour="*"), scheduler_task.s(), name="every hour")

@app.task
def scheduler_task():
    price_value = get_price("https://www.google.com/finance/quote/USD-UAH")
    save_toDb(price_value)
    
