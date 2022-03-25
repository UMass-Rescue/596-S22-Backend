#!/bin/sh

# Is the database read to accept connections?
# If the database is not ready to accept connections and this script proceeds regardless, the Docker container will crash.
# while [pg_isready -h db -p 5432 == ] do
#   sleep 1
# done

# # Run all migrations on the database.
# alembic upgrade head

# start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000