#!/bin/sh

while ! pg_isready 
do
    echo "$(date) - waiting for database to start"
    sleep 10
done

# # Run all migrations on the database.
alembic upgrade head

# until alembic upgrade head; do sleep 10; done

# start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000