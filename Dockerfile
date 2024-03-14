FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN flask db init

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV FLASK_APP=app.py

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]