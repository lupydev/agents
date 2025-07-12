#!/bin/sh
# Aplica las migraciones
alembic upgrade head

# Inicia el servidor de FastAPI con uvicorn
# uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

# Inicia el servidor con el cli de FastAPI
fastapi dev app/main.py --host 0.0.0.0 --port 8080