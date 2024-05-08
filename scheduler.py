from datetime import datetime, timedelta
from redis import Redis
from rq_scheduler import Scheduler
from .scraping import get_price
from .database import save_toDb

redis = Redis(host="localhost", port=6379)

scheduler = Scheduler(connection=redis)

def container() -> None:
    price_value = get_price("https://www.google.com/finance/quote/USD-UAH")
    save_toDb(price_value)
    
scheduler.schedule(
    scheduled_time=datetime.utcnow(),
    func=container,
    interval=timedelta(hours=1)
)
