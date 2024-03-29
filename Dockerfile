FROM python:3.9-alpine3.13
LABEL maintainer="saulyaka"
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /code/

VOLUME .:/code
