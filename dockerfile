FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/django-app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy the start.sh script into the container
COPY ./core/scripts/start.sh /app/django-app/core/scripts/start.sh

# Set the script as executable
RUN chmod +x /app/django-app/core/scripts/start.sh


EXPOSE 8000
