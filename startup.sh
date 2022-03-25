#!/bin/sh

while ! pg_isready -h "db" -p 5432
do
    echo "$(date) - waiting for database to start"
    sleep 5
done

# # Run all migrations on the database.
alembic upgrade head

# start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000