#!/bin/bash
set -e # Exit immediately if a command fails

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000
