FROM python:3.11

RUN apt-get update -y && \
    apt-get upgrade -y

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app
