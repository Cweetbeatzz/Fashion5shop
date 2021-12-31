FROM python:3.9-slim

WORKDIR /app/

COPY requirments/prod.txt ./requirments/prod.txt
RUN pip install -r ./requirements/prod.text

COPY manage.py ./manage.py
COPY fashion5 ./fashion5