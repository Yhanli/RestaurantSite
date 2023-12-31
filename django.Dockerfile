FROM python:3.11

RUN ["mkdir", "-p", "/src/app"]

WORKDIR /src/app
COPY ./requirements.txt /src/app

RUN pip install -r requirements.txt
