#!/usr/bin/env bash
# Render build script - stops on the first error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate --no-input

# Create/refresh the 68 menu items and point them at local images
python manage.py seed_menu
python manage.py fix_food_images

# Create the admin login once (skipped quietly if it already exists)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input || echo "Superuser already exists - skipping"
fi
