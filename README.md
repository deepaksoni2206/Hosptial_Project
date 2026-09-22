# Hospital_Project

## Overview
A production‑grade backend for the **Amrutam Telemedicine** platform built with Django and Django REST Framework. It provides APIs for user management, doctor scheduling, appointment booking, consultations, prescription handling, and a dummy payment flow.

## Features
- JWT based authentication & role‑based access control
- Doctor availability management with safe, idempotent booking (row‑level locking)
- Consultation and prescription CRUD APIs
- Mock payment processor for end‑to‑end testing
- Auto‑generated OpenAPI (Swagger) documentation
- Prometheus metrics & structured logging
- Comprehensive unit & integration tests (pytest)
- Containerized deployment with Docker & Docker‑Compose

## Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python 3.11, Django 5.2, Django REST Framework |
| Auth | `djangorestframework‑simplejwt` |
| DB | PostgreSQL (via `psycopg2‑binary`) |
| Docs | `drf‑spectacular` |
| Monitoring | `django‑prometheus` |
| Containerization | Docker, Docker‑Compose |
| Testing | pytest, pytest‑django |

## Getting Started

### Prerequisites
- Python 3.11
- Docker & Docker‑Compose (optional for containerized run)
- PostgreSQL (if not using Docker)

### Local Development
```bash
# Clone repo
git clone https://github.com/deepaksoni2206/Hosptial_Project.git
cd Hosptial_Project/Hospital

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate   # on Windows
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```
Open **http://127.0.0.1:8000/api/docs/** to explore the API.

### Docker Setup
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000/` and Prometheus at `http://localhost:9090/`.

## Testing
```bash
pytest
```
All tests should pass.

## Contributing
Contributions are welcome. Please open issues or pull requests following the conventional commit style.

## License
MIT License
