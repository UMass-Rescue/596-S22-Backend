FROM python:3.9

WORKDIR /rescue

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -f -y postgresql-client

RUN pip install --no-cache-dir --upgrade -r /rescue/requirements.txt

COPY alembic/ ./alembic/
COPY alembic.ini .
COPY startup.sh .

COPY ./app /rescue/app

# Run alembic configuration
CMD ["./startup.sh"]