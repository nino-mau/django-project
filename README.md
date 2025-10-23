# Django Project

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd django-project
```

### 2. Create your environment file

```bash
cp .env.example .env
```

Then update `.env` with your local configuration values.

## Start Development with Docker

Start the application using Docker Compose:

```bash
docker-compose up -d --build
```

Execute the migration:

```bash
docker compose exec django /app/manage.py makemigrations app
docker compose exec django /app/manage.py migrate
```

Generate static files:

```bash
docker compose exec django /app/manage.py collectstatic
```

Once built, the app will be available at **[http://localhost:8000](http://localhost:8000)**.

#### Optional LSP support

Install dependencies outside of container:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
