FROM python:3.9

WORKDIR /rescue

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /rescue/requirements.txt

# Run alembic configuration
CMD ["./startup.sh"]

COPY ./app /rescue/app