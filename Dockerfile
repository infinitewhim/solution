# Dockerfile

FROM python:3.8-slim

RUN mkdir /app/
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/
ENV PYTHONPATH /app
ENV FLASK_APP=server.py
CMD flask run -h 0.0.0.0 -p 5000