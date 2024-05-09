FROM python:3.8-slim

# Install necessary packages for GPIO
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "bme280-exporter.py"]