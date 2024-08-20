# Dockerfile for Network Monitor
# Version: 1.0

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY network_monitor.py .

CMD ["python", "network_monitor.py"]
