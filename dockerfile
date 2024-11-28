FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=web.settings \
    HOST=0.0.0.0 \
    PYTHONPATH=/app

EXPOSE 8000

CMD ["sh", "-c", \
    'echo "yes" | ./venv/bin/python manage.py collectstatic --noinput && \
    ./venv/bin/python manage.py makemigrations && \
    ./venv/bin/python manage.py migrate && \
    ./venv/bin/uvicorn web.asgi:application --host 0.0.0.0 --port 8000']