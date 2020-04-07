FROM python:3.7.7-alpine3.11

RUN mkdir /web
WORKDIR "/web"
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR "/web/src"
COPY ./src .
