FROM python:3.8-slim

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext

RUN python3 -m pip install -r requirements.txt

COPY . .
