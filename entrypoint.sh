#!/bin/bash
set -e # Exit immediately if a command fails

# Run migrations
python3 manage.py migrate

# Install Tailwind (if needed)
python3 manage.py tailwind install

# Start tailwind
python3 manage.py tailwind start &&

  # Start Django development server
  python3 manage.py runserver 0.0.0.0:8000
