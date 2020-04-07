FROM python:3.7.7-alpine3.11

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN mkdir /web
WORKDIR "/web"
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR "/web/src"
COPY ./src .

CMD sh run_script.sh
