#!/bin/sh

# Remove the migrations
echo "Removing migration files..."
find /mahware/applications -path "*/migrations/*.py" ! -name "__init__.py" -delete
find /mahware/applications -path "*/migrations/*.pyc" -delete

# Apply database migrations
echo "Making migrations file..."
python manage.py custom_makemigrations

#echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn in the foreground
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000

wait