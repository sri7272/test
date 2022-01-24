#https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
FROM python:3.9-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
