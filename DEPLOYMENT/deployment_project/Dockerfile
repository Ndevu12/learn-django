FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collectstatic does not need a real DB; SECRET_KEY only has to be non-empty at build time
ENV SECRET_KEY=dummy-build-only-not-used-at-runtime \
    DEBUG=False \
    ALLOWED_HOSTS=localhost \
    DJANGO_SETTINGS_MODULE=deployment_project.settings
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "deployment_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
