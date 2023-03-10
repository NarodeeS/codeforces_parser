FROM python:3.11

RUN apt-get update -y && \
    apt-get upgrade -y

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
