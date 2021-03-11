# pull official base image
FROM python:3.8.8-alpine

# allows cryptography installation
RUN python -m pip install --upgrade pip
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo

# set work directory
WORKDIR /usr/src/drf

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .