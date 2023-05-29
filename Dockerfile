FROM python:3.9-slim-buster

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt
COPY animegg /animegg
WORKDIR /animegg
EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user
