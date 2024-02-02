FROM python:3.11.5-slim-bookworm

WORKDIR /app

COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

WORKDIR /app/tree_menu

ENV PYTHONUNBUFFERED=1

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000