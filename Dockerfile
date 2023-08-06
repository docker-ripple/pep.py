FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3.9-dev python3.9-pip \
    gcc libmysqlclient-dev python3.9-setuptools

COPY requirements.txt requirements.txt
RUN python3.9 -m pip install -r requirements.txt

COPY . .
CMD python3.9 pep.py
