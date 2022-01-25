#https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
FROM python:3.9-slim

RUN pip install --no-cache-dir uwsgi

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app

#CMD ["python", "app.py"]
CMD ["uwsgi", "--http-socket", "0.0.0.0:5000", "-w", "app:app"]
