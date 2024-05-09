FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt /backend

RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

CMD ["sh", "-c", "python tgbot.py & python scheduler.py"]


