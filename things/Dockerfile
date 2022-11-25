FROM python:latest
WORKDIR /srv/source
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /srv/source/
RUN pip install -r requirements.txt
COPY . /srv/source/